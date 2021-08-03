# TwitterNotifications-Discord-Bot

This bot will send you a notification on your discord server anytime a specific twitter user makes a new tweet.

## How does it work?

Once the bot is given a twitter user, and the id of a discord channel, it'll start looking for new tweets of the user and, once it finds a new tweet, it will send a notification to the channel given.

## How to use?

Use this [link](https://discord.com/api/oauth2/authorize?client_id=871417926589243454&permissions=259846043712&scope=bot) to add the bot to a server of your choice.

Type '$notifuser < twitter @ >' to define which user you want to be notified about.

Type '$notifchannel < channel ID >' to define which channel should the notifications be sent to.

## How was this bot built?

This bot was made entirely using python, with the help of the tweepy and discordpy APIs.


