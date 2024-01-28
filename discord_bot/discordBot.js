const { Client, GatewayIntentBits, EmbedBuilder } = require('discord.js');
const { token } = require('../config.json'); // Ensure this path is correct for your setup
const axios = require('axios');
let fetchData;

// Create a new client instance
const client = new Client({ intents: [GatewayIntentBits.Guilds] });

// Define the 'ready' event handler
client.once('ready', async () => {
    console.log('Discord bot is ready!');
    // Dynamically import the fetchData function from the scrape module
    try {
        fetchData = (await import('../tools/scrape.js')).default;
    } catch (error) {
        console.error('Error importing the scrape module:', error);
    }
});

client.on('interactionCreate', async interaction => {
    if (!interaction.isCommand()) return;

    if (interaction.commandName === 'ask') {
        // Existing 'ask' command logic
        const question = interaction.options.getString('question');
        const userId = interaction.user.id; // Extract user ID from the interaction

        // Acknowledge the interaction immediately
        await interaction.deferReply();
        const channel = await client.channels.fetch(interaction.channelId);
        channel.sendTyping(); // Show typing indicator in the channel

        try {
            // Send the question and userId to your Express app
            const response = await axios.post('http://localhost:3000/chat', { message: question, userId });
            let reply = `Question: ${question}\nAnswer: ${response.data.response}`;

            // Simulate typing delay based on the length of the reply
            setTimeout(async () => {
                if (reply.length > 2000) {
                    await sendInParts(reply, interaction); // If the reply is too long, send it in parts
                } else {
                    await interaction.editReply(reply || 'No response from the assistant.');
                }
            }, calculateTypingDelay(reply));
        } catch (error) {
            console.error("Error in interaction with assistant:", error);
            await interaction.editReply('Sorry, there was an error processing your request.');
        }

    } else if (interaction.commandName === 'roll') {

        // Dice roll command logic
        const dice = interaction.options.getInteger('dice') || 1;
        const sides = interaction.options.getInteger('sides') || 6;
        const results = rollDice(dice, sides);

        const embed = new EmbedBuilder()
            .setColor(0x0099FF)
            .setTitle('🎲 Dice Roll')
            .setDescription(`Rolling ${dice} dice with ${sides} sides each.`)
            .addFields({ name: 'Results', value: results.join(', ') });

        await interaction.reply({ embeds: [embed] });

    } else if (interaction.commandName === 'npcgen') {
        const npcCount = interaction.options.getInteger('number');

        // Validate the input number
        if (npcCount < 1 || npcCount > 5) {
            return await interaction.reply('Please enter a number between 1 and 5.');
        }

        await interaction.deferReply(); // Acknowledge the command

        for (let i = 0; i < npcCount; i++) {
            const characterData = await fetchData('https://deorum.vercel.app/gallery/');
            const character = characterData[i % characterData.length]; // Loop over character data

            const description = character.description && character.description.trim() !== ''
                                ? character.description 
                                : 'No description available.';

            const characterEmbed = new EmbedBuilder()
                .setColor(0x00AE86)
                .setTitle(character.title || 'Unknown Title')
                .setDescription(description)
                .setImage(character.imageUrl || 'https://example.com/default-image.jpg')
                .setURL(character.detailsUrl || 'https://example.com');

            const customLabels = ['Race', 'Archetype', 'Background'];    

            character.features.forEach((feature, index) => {
                const label = customLabels[index] || 'Additional Feature';
                characterEmbed.addFields({ name: label, value: feature, inline: true });
            });

            await interaction.followUp({ content: `Character ${i + 1}`, embeds: [characterEmbed] });
        }
    }
});

function rollDice(numberOfDice, sides) {
    const rolls = [];
    for (let i = 0; i < numberOfDice; i++) {
        rolls.push(Math.floor(Math.random() * sides) + 1);
    }
    return rolls;
}

async function sendInParts(message, interaction) {
    const MAX_LENGTH = 2000;

    while (message.length > 0) {
        const breakPoint = findBreakPoint(message, MAX_LENGTH);
        const toSend = message.substring(0, breakPoint).trim();
        await interaction.followUp(toSend);
        await new Promise(resolve => setTimeout(resolve, 1000)); // 1 second delay

        message = message.substring(breakPoint).trim();
    }
}

function findBreakPoint(message, maxLength) {
    let breakPoint = findNearestSentenceEnd(message, maxLength) || findListEnd(message, maxLength);
    if (breakPoint === -1) { // No suitable sentence/list end found within the limit
        breakPoint = message.substring(0, maxLength).lastIndexOf(' ') + 1;
        if (breakPoint === 0 || message.length < maxLength) breakPoint = Math.min(message.length, maxLength);
    }
    return breakPoint;
}

function findNearestSentenceEnd(message, maxLength) {
    const regex = /[\.\?\!]\s/g;
    let lastValidIndex = -1;
    let match;

    while ((match = regex.exec(message)) !== null) {
        if (match.index + match[0].length <= maxLength) {
            lastValidIndex = match.index + match[0].length;
        } else {
            break;
        }
    }

    return lastValidIndex;
}

function findListEnd(message, maxLength) {
    const regex = /\d+\.\s/g;
    let lastFound = -1;
    let match;

    while ((match = regex.exec(message.substring(0, maxLength))) !== null) {
        lastFound = match.index + match[0].length;
    }

    return lastFound;
}

function calculateTypingDelay(message, typingSpeed = 120) {
    return Math.min(Math.max(message.length / typingSpeed * 1000, 1000), 5000); // Ensures delay is between 1 and 5 seconds
}

client.login(token);
