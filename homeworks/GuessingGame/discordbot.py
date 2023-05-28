import discord
import random
from discord.ext import commands

CLIENTID=input("Insert bot token:")
intents = discord.Intents.all()
client = commands.Bot(command_prefix=commands.when_mentioned, intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(aliases=['start'])
async def guess(ctx):
    number=random.randint(1,100)
    await ctx.send(number)
    await ctx.send('The game has started. \nGuess my number ranging from 1 to 100.')
    def check(m):
        return m.author == ctx.author and m.channel == ctx.message.channel
    for i in range(1,100):
        guess = await client.wait_for('message', check=check)
        try:
            int(guess.content)
            if guess.content == str(number):
                await ctx.send(f"You won! \nIt took you {i} tries to guess!")
                break
            if guess.content >= str(number):
                await ctx.send(f"Lower!")
            if guess.content <= str(number):
                await ctx.send(f"Higher!")
            if guess.content>100 or guess.content<1:
                await ctx.send(f"My number is ranged between 1 and 100! \nPlease enter a number in that range.")
        except:
            await ctx.send("Enter a number!")
            i-=1

client.run(CLIENTID)


