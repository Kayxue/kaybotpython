import discord
from discord.ext import commands
import random
import json

bot=commands.Bot(command_prefix='s!',help_command=None,description="由芝麻湯圓所製作的機器人")
client=discord.Client()

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

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
    embed1=discord.Embed(title='清理訊息成功！',description=f'成功清除{num}則訊息！',color=0xb6b8ba)
    await ctx.channel.send(embed=embed1)

@bot.command()
async def botinfo(ctx):
    embed1=discord.Embed(title='關於此機器人',description='關於此機器人的資訊',color=0xb6b8ba)
    await ctx.channel.send(embed=embed1)

@bot.command()
async def help(ctx):
    embed1=discord.Embed(title='幫助',description='指令清單',color=0xb6b8ba)
    embed1.add_field(name='botinfo',value='查看關於此機器人之資訊',inline=False)
    embed1.add_field(name='clear [欲清理之訊息數]',value='清除指定數量之訊息',inline=False)
    await ctx.channel.send(embed=embed1)

bot.run(jdata["TOKEN"])
