import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client = discord.Client()
bot_prefix = "-"
client = commands.Bot(command_prefix = bot_prefix)
status = cycle(['Anime', 'Chinese Cartoons'])


#COMMANDS-----------------------------------------
#PING

@client.command()
async def ping(ctx):
    await ctx.channel.send(f'Pong! {round(client.latency * 1000)}ms')

#TEST COMMAND
@client.command()
async def test(ctx):
    await ctx.send("Test")

#8BALL
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command')

#CLEAR MSGS
@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Enter the amount of messages you want to clear!')  

#EVENTS--------------------------------------

@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="Anime"))
    print('Bot is ready.')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))

#ON MESG
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    await client.process_commands(message)





client.run('token')
