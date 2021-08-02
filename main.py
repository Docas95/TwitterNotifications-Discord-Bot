import tweepy
from genshinBotENV import *
import discord
from discord.ext import tasks

# consumer keys and access token
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret
discord_token = discord_token

# start the twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

# this variable represents our discord bot
client = discord.Client()

# list that will store the user whose tweets we will search
user = [' ']

# list that will store the channel that receives notifications
channel = [' ']

# stores the last tweet sent
lastTweet = [' ']

# start a stream
def main():
    @client.event
    # code will execute once the bot is ready
    async def on_ready():
        print('We have logged in as ' + str(client.user))

    @tasks.loop(seconds = 10)
    # get the last tweet posted by the user, and then send it to discord
    async def stream(user, channel):
        channelNotif = client.get_channel(int(channel))
        for status in tweepy.Cursor(api.user_timeline, id=user).items(1):
            if status.id != lastTweet[0]:
                await channelNotif.send('@' + user + ' has made a new post!\n' + 'https://twitter.com/twitter/statuses/' + str(status.id))
                lastTweet[0] = status.id

    @client.event
    # code will execute when a message is detected
    async def on_message(message):
        msg = message.content

        # define the user whose tweets we want
        if msg.startswith('$notifuser'):
            if len(msg.split(' ')) == 2:
                user[0] = msg.split(' ')[1]
                print('Twitter user: @' + user[0])
                if channel[0] != ' ':
                    try:
                        stream.start(user[0], channel[0])
                    except:
                        stream.restart(user[0],channel[0])
        
        # define which channel the notification
        if msg.startswith('$notifchannel'):
            if len(msg.split(' ')) == 2:
                channel[0] = msg.split(' ')[1]
                print('Channel ID: ' + channel[0])
                if user[0] != ' ':
                    try:
                        stream.start(user[0], channel[0])
                    except:
                        stream.restart(user[0], channel[0])

    client.run(discord_token)
main()


