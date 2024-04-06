import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('OTI2MjI1OTE3NzE2NjExMTQ1.G75afy.Sgy8dRjnU08awxLlMUn50CvU43DNMKbEWznbXs')
