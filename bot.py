import discord
from discord.ext import commands
import random
import json
import os
from core.classes import *
from disputils import *

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class Bot(commands.Bot):
    def __init__(self):
        super(Bot,self).__init__(command_prefix=['s!','sesame '],help_command=None,description="由芝麻湯圓所製作的機器人")
        self.add_cog(maintask(self))
    
    async def on_ready(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Game(name='s!help / sesame help'))
        print('Bot is online')

class maintask(Cog_Extension):
    
    def is_it_me(ctx):
        return ctx.author.id == 470516498050580480
    
    @commands.command(pass_context = True)
    @commands.check(is_it_me)
    async def load(self,ctx,extension):
        bot.load_extension(f'cmds.{extension}')
        embed1=discord.Embed(title='指定類別指令載入成功！',description=f'成功載入{extension}類別指令！',color=0xb6b8ba)
        await ctx.send(embed=embed1)

    @load.error
    async def load_error(self,ctx,error):
        if isinstance(error,discord.ext.commands.CheckFailure):
            embed1=discord.Embed(title='權限不足！',description='只有湯圓本人能執行此指令喔！',color=0xb6b8ba)
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

    @commands.command()
    @commands.check(is_it_me)
    async def unload(self,ctx,extension):
        bot.unload_extension(f'cmds.{extension}')
        embed1=discord.Embed(title='指定類別指令解除載入成功！',description=f'成功解除載入{extension}類別指令！',color=0xb6b8ba)
        await ctx.send(embed=embed1)
        
    @unload.error
    async def unload_error(self,ctx,error):
        if isinstance(error,discord.ext.commands.CheckFailure):
            embed1=discord.Embed(title='權限不足！',description='只有湯圓本人能執行此指令喔！',color=0xb6b8ba)
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
        
    @commands.command()
    @commands.check(is_it_me)
    async def reload(self,ctx,extension):
        bot.reload_extension(f'cmds.{extension}')
        embed1=discord.Embed(title='已重新載入指定類別指令！',description=f'成功重新載入{extension}類別指令！',color=0xb6b8ba)
        await ctx.send(embed=embed1)
    
    @reload.error
    async def reload_error(self,ctx,error):
        if isinstance(error,discord.ext.commands.CheckFailure):
            embed1=discord.Embed(title='權限不足！',description='只有湯圓本人能執行此指令喔！',color=0xb6b8ba)
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

    @commands.command()
    async def help(self,ctx):
        embed=[discord.Embed(title='幫助－資訊類',description='資訊類指令表',color=0xb6b8ba)
                      .add_field(name='help',value='顯示此列表',inline=False)
                      .add_field(name='botinfo',value='查看關於此機器人之資訊',inline=False)
                      .add_field(name='userinfo',value='顯示出你的使用者資訊',inline=False)
                      .add_field(name='showtime',value='顯示當前所在時區之時間',inline=False),
               discord.Embed(title='幫助－休閒娛樂類',description='休閒娛樂類指令表',color=0xb6b8ba)
                      .add_field(name='say',value='讓bot說出指定訊息',inline=False)
                      .add_field(name='saydel',value='讓bot說出指定訊息（輸入之指令會被刪除）',inline=False)
                      .add_field(name='loly',value='隨機顯示一張蘿莉圖'),
               discord.Embed(title='幫助－伺服器資訊類',description='伺服器資訊類指令表，\n所有人能執行這些指令喔！',color=0xb6b8ba)
                      .add_field(name='serverinfo',value='查看此伺服器的資訊',inline=False)
                      .add_field(name='serverboost',value='查看此伺服器之加速狀態',inline=False),        
               discord.Embed(title='幫助－伺服器管理類',description='伺服器管理類指令表，\n要執行此類指令必須要有該指令相對應之權限',color=0xb6b8ba)
                      .add_field(name='clear',value='清除指定數量之訊息\n（必須權限：管理訊息）',inline=False)
                      .add_field(name='kick',value='將指定使用者踢出伺服器\n（必須權限：踢出成員）',inline=False)
                      .add_field(name='ban（請先不要用）',value='將指定使用者封鎖\n（必須權限：封鎖成員）',inline=False),
               discord.Embed(title='幫助－機器人管理類',description='機器人管理類指令表，\n僅湯圓本人能執行這些指令喔！\n這些為管理機器人載入之功能與指令的指令',color=0xb6b8ba)
                      .add_field(name='load',value='啟用指定類別之功能或指令',inline=False)
                      .add_field(name='reload',value='重新載入指定類別之功能或指令',inline=False)
                      .add_field(name='unload',value='關閉指定類別之功能或指令',inline=False)
               ]
        paginator = BotEmbedPaginator(ctx, embed)
        await paginator.run()

bot=Bot()

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])
