# bot.py
import os

import discord
from discord.ext import commands
from discord import Interaction
from discord.ext.commands import Context
from dotenv import load_dotenv, find_dotenv
import utils
import asyncio


poke_list = utils.get_evs()

load_dotenv(find_dotenv())
TOKEN = os.getenv('your token name')

intents = discord.Intents.all()

client = commands.Bot(command_prefix='$', intents=intents)

@client.command(
    help="$evs [Pokemon name]|[Pokemon idx (not the same in the Pokedex!)] -> EVs you get for fighting him"
)
async def evs(ctx: Context, pokemon):
    msg = utils.write_message(pokemon.lower(), poke_list)
    await ctx.channel.send(msg)

client.run("your token here")
