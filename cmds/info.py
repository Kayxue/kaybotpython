import discord
from discord.ext import commands
from core.classes import *
import datetime
from datetime import *

class Info(Cog_Extension):
    @commands.command()
    async def botinfo(self,ctx):
        embed1=discord.Embed(title='關於此機器人',description='關於此機器人的資訊',color=0xb6b8ba)
        await ctx.channel.send(embed=embed1)

    @commands.command()
    async def showtime(self,ctx):
        outtime=time.strftime("%Y/%m/%d %p %l:%M:%S %Z")
        await ctx.channel.send(outtime)

def setup(bot):
    bot.add_cog(Info(bot))