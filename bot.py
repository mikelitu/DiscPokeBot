# bot.py
import os

import discord
from discord.ext import commands
from discord import Interaction
from discord.ext.commands import Context
from dotenv import load_dotenv, find_dotenv
import utils
import pandas as pd


poke_df = pd.read_csv("pokemonData/Pokemon.csv")


load_dotenv(find_dotenv())
TOKEN = os.getenv('POKE_DISCORD_TOKEN')

intents = discord.Intents.all()

client = commands.Bot(command_prefix='$', intents=intents)

@client.command(
    help="$evs [Nombre del pokemon] -> Los EVs que te da al combatir"
)
async def evs(ctx: Context, pokemon):
    msg = utils.write_message_evs(pokemon, poke_df)
    await ctx.channel.send(msg)

@client.command(
    help="$stats [Nombre del pokemon] -> Stats del Pokemon"
)
async def stats(ctx: Context, pokemon):
    msg = utils.write_message_stats(pokemon, poke_df)
    await ctx.channel.send(msg)

client.run(TOKEN)