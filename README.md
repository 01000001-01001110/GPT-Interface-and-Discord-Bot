
# app.js
This is the main application file for our server. It is responsible for handling requests and responses, as well as managing the interaction with the OpenAI assistant.

## Key Features
OpenAI Assistant Interaction: The application communicates with the OpenAI assistant and processes its responses. If no response is received from the assistant, an error message is returned to the client.

### Error Handling: 
The application has robust error handling, logging any errors that occur during the processing of a chat and returning a server error response to the client.

### Lock Release: 
After processing a chat, the application releases a lock associated with the user ID. This ensures that multiple requests from the same user are processed in order.

### Server Setup: 
The application sets up a server that listens on a specified port. The port number is either provided by the environment variable PORT or defaults to 3000 if no environment variable is set.

### Port Configuration: 
The PORT environment variable is used to specify the port number on which the server should run. If no PORT variable is set, the server defaults to running on port 3000.

## .env
This file is used to store environment variables. These are often used to store sensitive information such as API keys, database URIs, and other credentials. In this case, it is used to store the port number on which the server should run.

ENV example: 

DISCORD_TOKEN=
OPENAI_API_KEY=
ASSISTANT_ID=
