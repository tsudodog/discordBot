import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix=".", intents=intents)
token = os.getenv("DISCORD_BOT_TOKEN")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Listening to .help"))
    print("I am online")


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./bot/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# @client.command()
# async def ping(ctx) :
#     await ctx.send(f"� Pong with {str(round(client.latency, 2))}")
#
# @client.command(name="whoami")
# async def whoami(ctx) :
#     print("who am i?")
#     await ctx.send(f"You are {ctx.message.author.name}")
#


client.run(token)
