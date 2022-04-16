import discord 
import os

client = discord.client()

@client.event
async def on_ready():
    print("Bot is now active")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.author != client.user:
        await message.channel.send("Yooo")

client.run(os.getenv('TOKEN'))