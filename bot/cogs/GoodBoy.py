import discord
import random
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Good Boy Cog Is loaded and ready")

    @commands.command(name="amiagoodboy")
    async def roll(self, ctx):
        """Determines if you are a good boy or not"""

        value = random.randint(0, 100)
        if value > 95:
            await ctx.send("Inflates you making you big and round")
        else:
            await ctx.send("You are a good boy.")


def setup(client):
    client.add_cog(Example(client))
