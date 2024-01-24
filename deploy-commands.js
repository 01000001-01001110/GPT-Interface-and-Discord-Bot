const { REST, Routes } = require('discord.js');
const { token } = require('./config.json'); // Only your bot token is needed here

const commands = [{
  name: 'ask',
  description: 'Ask a question to the assistant',
  options: [{
    name: 'question',
    type: 3,
    description: 'The question you want to ask',
    required: true,
  }],
}];

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
