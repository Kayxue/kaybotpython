import discord
from discord.ext import commands
from core.classes import *
import datetime
from datetime import *
import pyowm

owm=pyowm.OWM("512f3f992f903e7611a229fcc2c06f53")

class Info(Cog_Extension):
    '''Bot資訊'''
    @commands.command()
    async def botinfo(self,ctx):
        embed1=discord.Embed(title="關於此機器人",description="關於此機器人的資訊",color=0xb6b8ba)
        embed1.add_field(name='擁有者：',value="芝麻湯圓")
        embed1.add_field(name='主要協助：',value='Harry the Gamer - AzureX1212')
        embed1.add_field(name='使用discord.py版本：',value=f"{discord.__version__}({discord.version_info[3]})")
        await ctx.channel.send(embed=embed1)
    '''時間資訊'''
    @commands.command()
    async def showtime(self,ctx):
        outtime=datetime.now().strftime("%Y/%m/%d %p %I:%M:%S %Z")
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
        embed1.add_field(name='加入此伺服器日期：',value=ctx.author.joined_at.strftime('%Y/%m/%d %p %I:%M:%S %Z'),inline=False)
        embed1.add_field(name='帳戶創建日期：',value=ctx.author.created_at.strftime('%Y/%m/%d %p %I:%M:%S %Z'),inline=False)
        embed1.set_thumbnail(url=ctx.author.avatar_url)
        embed1.set_footer(text=ctx.author,icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed1)
        
    @commands.command()
    async def weather(self,ctx,location:str):
        observation=owm.weather_at_place(location)
        w=observation.get_weather()
        weather=w.get_detailed_status()
        temps=w.get_temperature(unit='celsius')
        embed1=discord.Embed(title="天氣資訊",description="該地天氣資訊如下：",color=0xb6b8ba)
        embed1.add_field(name="天氣",value=weather)
        embed1.add_field(name="目前溫度",value=f"{temps['temp']}\u2103")
        embed1.add_field(name="最高溫度",value=f"{temps['temp_max']}\u2103")
        embed1.add_field(name="最低溫度：",value=f"{temps['temp_min']}\u2103")
        embed1.set_footer(icon_url="https://pbs.twimg.com/profile_images/1173919481082580992/f95OeyEW_400x400.jpg",text="資料提供：openweathermap.org")
        await ctx.channel.send(embed=embed1)
        

def setup(bot):
    bot.add_cog(Info(bot))