import ctypes
import datetime
import ftplib
import json
import math
# import pathlib
import shlex
import time
from threading import Thread
from urllib.parse import urlparse
import subprocess as sp
import discord
import os
import re

import unicodedata
import asyncio

import interactions
import dis

from os.path import exists
from discord.ext import commands


with open('config.json', encoding="utf8") as json_file:
    global Config
    Config = json.load(json_file)


prefix = Config["command_prefix"]

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=prefix, intents=intents)

@client.command(
    name="chat",
    description="chat via bot",
    # scope=the_id_of_your_guild,@client.command(
    options = [
        interactions.Option(
            name="message",
            description="Message to be sent",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def chat(ctx: interactions.CommandContext, message):
    await ctx.channel.send(message)


@client.event
async def on_ready():
    # await tree.sync(guild=discord.Object(id=Config["guild_id"]))
    print(f"logged in as {client}")
    asyncio.create_task(live_status())


async def live_status():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=f'{client.get_guild(902755443649179679).member_count} Members'))


client.run(Config["token"])

