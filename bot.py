import discord
from discord.ext import commands
import random

bot=commands.Bot(command_prefix='s!')
client=discord.Client()


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines.strip[0]


token = readtoken()


@bot.event
async def on_ready():
    print('Bot is online')


@bot.event
async def on_member_join(member):
    channel=discord.utils.get(member.guild.channels,name="歡迎welcome")
    embed1=discord.Embed(title='歡迎新成員！',description=f'歡迎{member.mention}來到此伺服器！',color=0xffffff)
    embed1.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed1)


@bot.event
async def on_member_remove(member):
    channel=discord.utils.get(member.guild.channels,name="歡迎welcome")
    embed2=discord.Embed(title='向成員說再見！',description=f'{member}離開了此伺服器，再見！{member}！',color=0xffffff)
    embed2.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed2)


@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice
    await bot.join_voice_channel(channel)


@bot.command()
async def leave(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()


@bot.command()
async def clear(ctx,num:int):
    await ctx.channel.purge(limit=num+1)


bot.run(token)
