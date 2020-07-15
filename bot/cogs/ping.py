import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client

    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.send(f'Pong! {round(self.client.latency * 1000)}ms')


def setup(client):
    client.add_cog(Ping(client))