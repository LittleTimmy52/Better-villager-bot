import os
import discord
from discord.ext import commands

prefix = "!!"

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
  print("{0.user} is online".format(bot))

@bot.command()
async def test(ctx):
  await ctx.message.delete()
  await ctx.send("test")

token = os.environ['TOKEN']
bot.run(token)