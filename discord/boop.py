#!/usr/bin/python3
"""
Started with
@see https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-bot
"""
import os
import time  # for sleeping
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # there is a file called `.env` that contains DISCORD_TOKEN='here'

client = discord.Client()
client.intents.members = True  # allows us to get list of the users


@client.event
async def on_ready():
    print(f'{client.user} has awoken!')


@client.event
async def on_message(message):
    if message.content == "!run":
        if 'purgatory' in [channel.name for channel in message.guild.channels]:
            await message.reply("Already done that\nNice Try")
        else:
            channel = await message.guild.create_text_channel('purgatory')  # @TODO send them a "welcome" message
            vchannel = await message.guild.create_voice_channel('purgatory')

        if "purgatory" not in [role.name for role in message.guild.roles]:
            cr = await message.guild.create_role(name="purgatory")

        # @TODO assign all members to purgatory role and remove others
        # @TODO or set role of other channels to be something else

    elif message.content == "!clean":
        await message.reply("Cleaning up & restoring server")
        time.sleep(3)
        await message.channel.send("lol jk")
    elif message.content == "!super_secret_command":
        await message.reply("Nice! one sec")
        time.sleep(1)  # @a nice delay
        for role in message.guild.roles:
            if role.name == "purgatory":
                await role.delete()  # manage_roles permission needed
        for channel in message.guild.channels:
            if channel.name == "purgatory":
                await channel.delete()


client.run(TOKEN)
