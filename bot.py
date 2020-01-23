import discord
from discord.ext import commands
import random
import json
import datetime
from datetime import *

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
    embed1=discord.Embed(title='歡迎新成員！',description=f'歡迎{member.mention}來到此伺服器！',color=0xb6b8ba)
    embed1.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed1)

@bot.event
async def on_member_remove(member):
    channel=discord.utils.get(member.guild.channels,name="歡迎welcome")
    embed2=discord.Embed(title='向成員說再見！',description=f'{member}離開了此伺服器，再見！{member}！',color=0xb6b8ba)
    embed2.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed2)
    
@bot.event
async def on_message_edit(before, after):
    userID=before.author.id
    channel=discord.utils.get(before.guild.channels,name="sesame-log")
    embed1=discord.Embed(title='訊息已編輯',description='有使用者編輯了他的訊息',color=0xb6b8ba)
    embed1.add_field(name='使用者：',value=f"{before.author.mention}",inline=False)
    embed1.add_field(name='於頻道：',value=f"#{before.channel}",inline=False)
    embed1.add_field(name='修改前：',value=f"{before.content}",inline=True)
    embed1.add_field(name='修改後：',value=f"{after.content}",inline=True)
    embed1.set_thumbnail(url=before.author.avatar_url)
    embed1.timestamp(value=f'{datetime.now().year}/{datetime.now().month}/{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}')
    embed1.set_footer(text=before.author,icon_url=before.author.avatar_url)
    await channel.send(embed=embed1)

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
@commands.has_permissions(manage_messages=True)
async def clear(ctx,num:int):    
    await ctx.channel.purge(limit=num+1)
    embed1=discord.Embed(title='清理訊息成功！',description=f'成功清除{num}則訊息！',color=0xb6b8ba)
    await ctx.channel.send(embed=embed1)

@clear.error
async def clear_error(ctx,error):
    if isinstance(error,discord.ext.commands.CheckFailure):
        embed1=discord.Embed(title='權限不足！',description='您沒有權限執行此指令！',color=0xb6b6ba)
        embed1.add_field(name='請確認您是否有以下權限：',value='管理訊息')
        await ctx.channel.send(embed=embed1)
    elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
        embed1=discord.Embed(title='請輸入要清除之訊息數量！',description='不會用嗎？沒關係，我幫你',color=0xb6b8ba)
        embed1.add_field(name='用法',value='``s!clear [要清除之訊息數量]``')
        embed1.add_field(name='範例',value='``s!clear 5``')
        await ctx.channel.send(embed=embed1)
    else:
        embed1=discord.Embed(title='清除失敗！',description='對不起，無法清除',color=0xb6b8ba)
        await ctx.channel.send(embed=embed1)

@bot.command()
async def botinfo(ctx):
    embed1=discord.Embed(title='關於此機器人',description='關於此機器人的資訊',color=0xb6b8ba)
    await ctx.channel.send(embed=embed1)

@bot.command()
async def help(ctx):
    embed1=discord.Embed(title='幫助',description='指令清單',color=0xb6b8ba)
    embed1.add_field(name='botinfo',value='查看關於此機器人之資訊',inline=False)
    embed1.add_field(name='clear',value='清除指定數量之訊息',inline=False)
    await ctx.channel.send(embed=embed1)

@bot.command()
async def time(ctx):
    year,month,day,hour,minute,second=datetime.now().year,datetime.now().month,datetime.now().day,datetme.now().hour,datetime.now().minute,datetime.now().second
    
def addzero(inputstr):
    x=str(inputstr)
    if len(inputstr) == 1:
        x="0"+x
        return x
    else:
        return x
bot.run(jdata["TOKEN"])
