import discord
import os

txtlogging_enabled = True # lol
token = "REPLACEME" # replace this with your token

client = discord.Client()

if not os.path.exists('logs'):
    os.makedirs('logs')

@client.event
async def on_message(message):
    if txtlogging_enabled == True:
        guild = message.guild
    if guild:
        path = "logs/{}.txt".format(guild.name)
        with open(path, 'a+', encoding='utf-8') as f:
            print("User: {0.author.name} Said: {0.content} | in {0.channel.name}".format(message), file=f)

client.run(token, bot=False)
