import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

class Clear(commands.Cog):

    def __init__(self,client):
        self.client = client

    #Commands
    @commands.command()
    async def clear(self, ctx, amount):
        await ctx.channel.purge(limit=amount+1)
    '''
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Enter the amount of messages you want to clear!')  
    '''

def setup(client):
    client.add_cog(Clear(client))