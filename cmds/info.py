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

def setup(bot):
    bot.add_cog(Info(bot))