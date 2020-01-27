import discord
from discord.ext import commands
from core.classes import *
import datetime
from datetime import *

class Info(Cog_Extension):
    @commands.command()
    async def botinfo(self,ctx):
        embed1=discord.Embed(title="關於此機器人",description="關於此機器人的資訊",color=0xb6b8ba)
        embed1.add_field(name='擁有者：',value="芝麻湯圓")
        embed1.add_field(name='主要協助：',value='Harry the Gamer - AzureX1212')
        embed1.add_field(name='使用discord.py版本：',value=f"{discord.__version__}({discord.version_info[3]})")
        await ctx.channel.send(embed=embed1)

    @commands.command()
    async def showtime(self,ctx):
        outtime=time.strftime("%Y/%m/%d %p %l:%M:%S %Z")
        await ctx.channel.send(outtime)
        
    @commands.command()
    async def userinfo(self,ctx):
        embed1=discord.Embed(title='使用者資訊',description='關於此使用者的資訊',color=0xb6b8ba)
        embed1.add_field(name='使用者名稱：',value=ctx.author,inline=False)
        embed1.add_field(name='在此群之暱稱：',value=ctx.author.nick,inline=False)
        embed1.add_field(name='使用者ID：',value=ctx.author.id,inline=False)
        if str(ctx.author.status) == 'dnd':
            embed1.add_field(name='狀態：',value='不要打擾我喔~~',inline=False)
        elif str(ctx.author.status) == 'idle':
            embed1.add_field(name='狀態：',value='悠閒中~~',inline=False)
        elif str(ctx.author.status) == 'online':
            embed1.add_field(name='狀態：',value='在線中，趕快找我聊天吧！',inline=False)
        elif str(ctx.author.status) == 'offline':
            embed1.add_field(name='狀態：',value='Sorry，我不在線，晚點喔！',inline=False)
        embed1.add_field(name='此伺服器之最高身份組：',value=ctx.author.top_role.mention,inline=False)
        embed1.add_field(name='帳戶創立日期：',value=ctx.author.joined_at,inline=False)
        embed1.set_thumbnail(url=ctx.author.avatar_url)
        embed1.set_footer(text=ctx.author,icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed1)
def setup(bot):
    bot.add_cog(Info(bot))