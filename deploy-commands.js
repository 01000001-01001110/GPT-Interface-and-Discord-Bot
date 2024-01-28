import { REST, Routes } from 'discord.js';
import config from './config.json' assert { type: 'json' };

const token = config.token;

const commands = [
  {
    name: 'ask',
    description: 'Ask a question to the assistant',
    options: [{
      name: 'question',
      type: 3,
      description: 'The question you want to ask',
      required: true,
    }],
  },
  {
    name: 'roll',
    description: 'Roll dice',
    options: [
      {
        name: 'dice',
        type: 4, // Corresponds to INTEGER type
        description: 'Number of dice to roll',
        required: false, // Make this optional; default can be set in the bot code
      },
      {
        name: 'sides',
        type: 4, // Corresponds to INTEGER type
        description: 'Number of sides on each die',
        required: false, // Make this optional; default can be set in the bot code
      }
    ]
  },
  {
    name: 'npcgen',
    description: 'Generate NPC characters',
    options: [
      {
        type: 4, // Corrected type value (INTEGER)
        name: 'number',
        description: 'Number of NPCs to generate (1-5)',
        required: true
      }
    ]
  }
];

const rest = new REST({ version: '9' }).setToken(token);

(async () => {
  try {
    console.log('Started refreshing application (/) commands globally.');
    await rest.put(
      Routes.applicationCommands("1197652049043660842"), // Replace with your actual application ID
      { body: commands },
    );
    console.log('Successfully reloaded application (/) commands globally.');
  } catch (error) {
    console.error(error);
  }
})();
