import express from "express";
import bodyParser from "body-parser";
import OpenAI from "openai";
import dotenv from "dotenv";
import morgan from "morgan";

dotenv.config();

const app = express();
app.use(bodyParser.json());
app.use(morgan("combined"));

const apiKey = process.env.OPENAI_API_KEY;
const openai = new OpenAI(apiKey);
const assistantId = process.env.ASSISTANT_ID;

let threadStore = {};
const locks = new Map();

async function acquireLock(userId) {
  return new Promise(resolve => {
    function tryAcquire() {
      if (!locks.get(userId)) {
        locks.set(userId, true);
        resolve();
      } else {
        setImmediate(tryAcquire); // Retry until the lock is acquired
      }
    }
    tryAcquire();
  });
}

function releaseLock(userId) {
  locks.delete(userId);
}

app.post("/chat", async (req, res) => {
  const { message, userId } = req.body;
  console.log(`Received message from userId ${userId}: ${message}`);

  if (!message) {
    console.log("Error: Message is required.");
    return res.status(400).json({ error: "Message is required" });
  }

  await acquireLock(userId); // Acquire lock for the current userId

  try {
    let { threadId } = threadStore[userId] || {};

    if (!threadId) {
      console.log(`No existing thread for userId ${userId}, creating new thread.`);
      const threadResponse = await openai.beta.threads.create();
      threadId = threadResponse.id;
      threadStore[userId] = { threadId };
      console.log(`New thread created with threadId ${threadId} for userId ${userId}`);
    } else {
      console.log(`Using existing threadId ${threadId} for userId ${userId}`);
    }

    console.log(`Sending user message to OpenAI for threadId ${threadId}`);
    const userMessageResponse = await openai.beta.threads.messages.create(threadId, { role: "user", content: message });
    console.log(`User message sent, OpenAI response: ${JSON.stringify(userMessageResponse)}`);

    console.log(`Creating run for threadId ${threadId}`);
    const runResponse = await openai.beta.threads.runs.create(threadId, { assistant_id: assistantId });
    const runId = runResponse.id;

    let run = await openai.beta.threads.runs.retrieve(threadId, runId);
    console.log(`Checking run status for runId ${runId} in threadId ${threadId}`);

    while (run.status !== "completed") {
      console.log(`Run status ${run.status}, waiting for completion...`);
      await new Promise(resolve => setTimeout(resolve, 1000));
      run = await openai.beta.threads.runs.retrieve(threadId, runId);
    }

    console.log(`Run completed for runId ${runId}, retrieving messages.`);
    const messagesResponse = await openai.beta.threads.messages.list(threadId);
    console.log(`Retrieved messages from threadId ${threadId}`);

    const latestAssistantResponse = messagesResponse.data
      .reverse() // Reverse to start checking from the latest message
      .find(msg => msg.role === 'assistant' && msg.created_at > userMessageResponse.created_at);

    if (!latestAssistantResponse) {
      console.log("No latest assistant message found.");
      return res.status(404).json({ error: "No response from OpenAI." });
    }

    console.log(`Latest assistant message ID: ${latestAssistantResponse.id}`);
    let response = latestAssistantResponse.content
      .filter(contentItem => contentItem.type === 'text')
      .map(textContent => textContent.text.value)
      .join('\n');

    console.log(`Sending response to user: ${response}`);
    res.json({ response });
  } catch (error) {
    console.error("Error processing chat:", error);
    res.status(500).json({ error: "Internal server error" });
  } finally {
    releaseLock(userId); // Release lock after processing
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
