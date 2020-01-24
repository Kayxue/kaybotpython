import discord
from discord.ext import commands
from core.classes import *


class Moderation(Cog_Extension):
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,num:int):    
        await ctx.channel.purge(limit=num+1)
        embed1=discord.Embed(title='清理訊息成功！',description=f'成功清除{num}則訊息！',color=0xb6b8ba)
        await ctx.channel.send(embed=embed1)

    @clear.error
    async def clear_error(self,ctx,error):
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

def setup(bot):
    bot.add_cog(Moderation(bot))