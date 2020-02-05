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
            embed1.add_field(name='錯誤訊息：',value=error)
            await ctx.channel.send(embed=embed1)
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,user:discord.Member,*,reason:str="未填寫"):
        channel=discord.utils.get(user.guild.channels,name="sesame-log")
        userID=user.id
        embed1=discord.Embed(title='踢出成員',description='指定成員已成功被踢出！',color=0xb6b8ba)
        embed1.add_field(name='踢出成員：',value=user.mention,inline=True)
        embed1.add_field(name='執行者：',value=ctx.message.author.mention,inline=True)
        embed1.add_field(name='原因：',value=reason,inline=False)
        embed1.set_thumbnail(url=user.avatar_url)
        embed1.set_footer(text=ctx.message.author,icon_url=ctx.message.author.avatar_url)
        await user.kick(reason=reason)
        embed2=discord.Embed(title='成功踢出成員！',description=f'已成功踢出成員：{user.mention}！',color=0xb6b8ba)
        await channel.send(embed=embed1)
        await ctx.channel.send(embed=embed2)
    
    @kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error,discord.ext.commands.CheckFailure):
            embed1=discord.Embed(title='權限不足！',description='您沒有權限執行此指令！',color=0xb6b6ba)
            embed1.add_field(name='請確認您是否有以下權限：',value='踢出成員')
            await ctx.channel.send(embed=embed1)
        elif isinstance(error, discord.ext.commands.BadArgument):
            userID=ctx.message.author.id
            embed1=discord.Embed(title='踢出失敗！',description='對不起，找不到此成員')
            await ctx.channel.send(embed=embed1)
        elif isinstance(error,discord.ext.commands.MissingRequiredArgument):
            embed1=discord.Embed(title='請輸入要踢出之成員！',description='不會用嗎？沒關係，我幫你',color=0xb6b8ba)
            embed1.add_field(name='用法',value='``s!kick [提及欲踢出之成員] [原因（選用）]``')
            embed1.add_field(name='範例',value='``s!kick @Dancing Sky 測試``')
            await ctx.channel.send(embed=embed1)
        else:
            embed1=discord.Embed(title='踢出失敗！',description='對不起，無法踢出成員',color=0xb6b8ba)
            embed1.add_field(name='錯誤訊息：',value=error)
            await ctx.channel.send(embed=embed1)
            
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,user:discord.Member,*,reason:str="未填寫"):
        channel=discord.utils.get(user.guild.channels,name="sesame-log")
        userID=user.id
        embed1=discord.Embed(title='封鎖成員',description='指定成員已成功被封鎖！',color=0xb6b8ba)
        embed1.add_field(name='封鎖成員：',value=user.mention,inline=True)
        embed1.add_field(name='執行者：',value=ctx.message.author.mention,inline=True)
        embed1.add_field(name='原因：',value=reason,inline=False)
        embed1.set_thumbnail(url=user.avatar_url)
        embed1.set_footer(text=ctx.message.author,icon_url=ctx.message.author.avatar_url)
        await user.ban(reason=reason,delete_message_date=30)
        embed2=discord.Embed(title='成功封鎖成員！',description=f'已成功封鎖成員：{user.mention}！',color=0xb6b8ba)
        await channel.send(embed=embed1)
        await ctx.channel.send(embed=embed2)
    
    @ban.error
    async def ban_error(self,ctx,error):
        if isinstance(error,discord.ext.commands.CheckFailure):
            embed1=discord.Embed(title='權限不足！',description='您沒有權限執行此指令！',color=0xb6b6ba)
            embed1.add_field(name='請確認您是否有以下權限：',value='封鎖成員')
            await ctx.channel.send(embed=embed1)
        elif isinstance(error, discord.ext.commands.BadArgument):
            userID=ctx.message.author.id
            embed1=discord.Embed(title='封鎖失敗！',description='對不起，找不到此成員')
            await ctx.channel.send(embed=embed1)
        elif isinstance(error,discord.ext.commands.MissingRequiredArgument):
            embed1=discord.Embed(title='請輸入要封鎖之成員！',description='不會用嗎？沒關係，我幫你',color=0xb6b8ba)
            embed1.add_field(name='用法',value='``s!ban [提及欲封鎖之成員] [原因（選用）]``')
            embed1.add_field(name='範例',value='``s!ban @Dancing Sky 測試``')
            await ctx.channel.send(embed=embed1)
        else:
            embed1=discord.Embed(title='封鎖失敗！',description='對不起，無法封鎖成員',color=0xb6b8ba)
            embed1.add_field(name='錯誤訊息：',value=error)
            await ctx.channel.send(embed=embed1)

def setup(bot):
    bot.add_cog(Moderation(bot))