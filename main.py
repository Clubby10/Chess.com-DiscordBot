const Discord = require('discord.js');
const client = new Discord.Client();
const axios = require('axios');

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', message => {
  if (message.content.startsWith('!chess')) {
    const username = message.content.split(' ')[1];
    axios.get(`https://api.chess.com/pub/player/${username}/stats`)
      .then(response => {
        const data = response.data;
        message.channel.send(`Username: ${data.username}\nRating: ${data.rating}\nGames Played: ${data.games_count}`);
      })
      .catch(error => {
        console.log(error);
        message.channel.send('There was an error retrieving data from the Chess.com API.');
      });
  }
});

client.login('YOUR_BOT_TOKEN_HERE');
