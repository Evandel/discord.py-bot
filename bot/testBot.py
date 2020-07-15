import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client = discord.Client()
bot_prefix = "-"
client = commands.Bot(command_prefix = bot_prefix)
status = cycle(['Anime', 'Chinese Cartoons'])

@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="Start up"))
    print('Bot is ready.')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))

@client.event
async def on_command_error(ctx, error):
    pass 


#ON MESG
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    await client.process_commands(message)

#COGS
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded "{extension}"')
    print(f'Loaded "{extension}"')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Reloading "{extension}"')
    print(f'Reloading "{extension}"')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded "{extension}"')
    print(f'Loaded "{extension}"')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded "{extension}"')
    print(f'Unoaded "{extension}"')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')




client.run('NzI5ODY1MTk0ODU5MjY2MTE5.XwZItQ.nCZuKQo8OVDdbIP0cLmOUi3-WIk')
