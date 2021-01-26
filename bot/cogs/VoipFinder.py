import discord

from discord.ext import commands


class VoipFinder(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("VoipFinder is ready.")

    # @commands.command()
    # async def ping2(self, ctx):
    #     await ctx.send(f"pong2")

    @commands.command(name="matchPrep")
    async def match_prep(self, ctx, team1: str, team2: str):
        guild = ctx.guild
        await ctx.send(""+team1+"\t"+team2+"\t")

def setup(client):
    client.add_cog(VoipFinder(client))
