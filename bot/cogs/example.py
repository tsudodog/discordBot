import discord
import random
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Example Cog Is loaded and ready")

    @commands.command()
    async def ping2(self, ctx):
        await ctx.send(f"pong2")

    @commands.command(name="roll")
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN')
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

def setup(client):
    client.add_cog(Example(client))
