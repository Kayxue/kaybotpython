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
@commands.has_permissions(manage_server=True)
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    embed1=discord.Embed(title='指定類別指令載入成功！',description=f'成功載入{extension}類別指令！',color=0xb6b8ba)
    await ctx.send(embed=embed1)

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    embed1=discord.Embed(title='指定類別指令解除載入成功！',description=f'成功解除載入{extension}類別指令！',color=0xb6b8ba)
    await ctx.send(embed=embed1)
    
@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    embed1=discord.Embed(title='已重新載入指定類別指令！',description=f'成功重新載入{extension}類別指令！',color=0xb6b8ba)
    await ctx.send(embed=embed1)

@bot.command()
async def help(ctx):
    embed1=discord.Embed(title='幫助',description='指令清單',color=0xb6b8ba)
    embed1.add_field(name='botinfo',value='查看關於此機器人之資訊',inline=False)
    embed1.add_field(name='clear',value='清除指定數量之訊息',inline=False)
    await ctx.channel.send(embed=embed1)

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])
