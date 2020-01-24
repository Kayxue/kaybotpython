import discord
from discord.ext import commands
import random
import json
import os

bot=commands.Bot(command_prefix='s!',help_command=None,description="由芝麻湯圓所製作的機器人")
client=discord.Client()

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

@bot.event
async def on_ready():
    print('Bot is online')

@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    embed1=discord.Embed(title='指定類別指令載入成功！',description=f'成功載入{extension}類別指令！',color=0xb6b8ba)
    await ctx.send(embed=embed1)

@load.error
async def load_error(ctx,error):
    if isinstance(error,discord.ext.commands.CheckFailure):
        embed1=discord.Embed(title='權限不足！',description='您沒有權限執行此指令！',color=0xb6b8ba)
        embed1.add_field(name='請確認您是否有以下權限：',value='管理員')
        await ctx.channel.send(embed=embed1)
    elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
        embed1=discord.Embed(title='請輸入要載入之類別！',description='不會用嗎？沒關係，我幫你',color=0xb6b8ba)
        embed1.add_field(name='用法',value='``s!load [類別名稱]``')
        embed1.add_field(name='範例',value='``s!load event``')
        await ctx.channel.send(embed=embed1)
    else:
        embed1=discord.Embed(title='載入失敗！',description='對不起，無法載入該類別之指令',color=0xb6b8ba)
        embed1.add_field(name='錯誤碼',value=error,inline=False)
        await ctx.channel.send(embed=embed1)

@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    embed1=discord.Embed(title='指定類別指令解除載入成功！',description=f'成功解除載入{extension}類別指令！',color=0xb6b8ba)
    await ctx.send(embed=embed1)
    
@unload.error
async def unload_error(ctx,error):
    if isinstance(error,discord.ext.commands.CheckFailure):
        embed1=discord.Embed(title='權限不足！',description='您沒有權限執行此指令！',color=0xb6b8ba)
        embed1.add_field(name='請確認您是否有以下權限：',value='管理員')
        await ctx.channel.send(embed=embed1)
    elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
        embed1=discord.Embed(title='請輸入要解除載入之類別！',description='不會用嗎？沒關係，我幫你',color=0xb6b8ba)
        embed1.add_field(name='用法',value='``s!unload [類別名稱]``')
        embed1.add_field(name='範例',value='``s!unload event``')
        await ctx.channel.send(embed=embed1)
    else:
        embed1=discord.Embed(title='解除載入失敗！',description='對不起，無法解除載入該類別之指令',color=0xb6b8ba)
        embed1.add_field(name='錯誤碼',value=error,inline=False)
        await ctx.channel.send(embed=embed1)
    
@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    embed1=discord.Embed(title='已重新載入指定類別指令！',description=f'成功重新載入{extension}類別指令！',color=0xb6b8ba)
    await ctx.send(embed=embed1)
    
@reload.error
async def reload_error(ctx,error):
    if isinstance(error,discord.ext.commands.CheckFailure):
        embed1=discord.Embed(title='權限不足！',description='您沒有權限執行此指令！',color=0xb6b8ba)
        embed1.add_field(name='請確認您是否有以下權限：',value='管理員')
        await ctx.channel.send(embed=embed1)
    elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
        embed1=discord.Embed(title='請輸入要重新載入之類別！',description='不會用嗎？沒關係，我幫你',color=0xb6b8ba)
        embed1.add_field(name='用法',value='``s!reload [類別名稱]``')
        embed1.add_field(name='範例',value='``s!reload event``')
        await ctx.channel.send(embed=embed1)
    else:
        embed1=discord.Embed(title='重新載入失敗！',description='對不起，不明原因，無法重新載入該類別之指令',color=0xb6b8ba)
        embed1.add_field(name='錯誤碼',value=error,inline=False)
        await ctx.channel.send(embed=embed1)

@bot.command()
async def help(ctx):
    embed1=discord.Embed(title='幫助',description='指令清單',color=0xb6b8ba)
    embed1.add_field(name='botinfo',value='查看關於此機器人之資訊',inline=False)
    embed1.add_field(name='clear',value='清除指定數量之訊息',inline=False)
    embed1.add_field(name='kick',value='將指定使用者踢出伺服器',inline=False)
    await ctx.channel.send(embed=embed1)

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])
