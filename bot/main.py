import discord
from discord.ext import commands
from quart import Quart, websocket, request

import os

app = Quart(__name__)


@app.route("/")
async def hello():
    await client.get_channel(799135266136129566).send("woof")
    return {"message": "sent"}


@app.route("/", methods=['POST'])
async def main_post():
    body = await request.get_json()
    app.logger.info(body)
    return {"status": body}


@app.route("/discord_auth", methods=['GET', 'POST'])
async def handle_oauth():
    body = await request.get_json()

    return {"status": 200, "body": body, "args": request.args}

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

client.loop.create_task(app.run_task('0.0.0.0', 5000))
client.run(token)
