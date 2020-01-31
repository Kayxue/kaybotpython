import discord
from discord.ext import commands
from core.classes import *
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class Fun(Cog_Extension):
    @commands.command()
    async def say(self,ctx,*,msg):
        if str(msg) not in jdata['AUTORESPONDKEYWORD']:
            await ctx.channel.send(msg)
        elif ctx.channel.name=='和湯圓說說話':
            await ctx.channel.send(f'{ctx.author.mention}：{msg}')
    
    @commands.command()
    async def saydel(self,ctx,*,msg):
        await ctx.message.delete()    
        if str(msg) not in jdata['AUTORESPONDKEYWORD']:
            await ctx.channel.send(msg)
        elif ctx.channel.name=='和湯圓說說話':
            await ctx.channel.send(f'{ctx.author.mention}：{msg}')
    
    @commands.command()
    async def loly(self,ctx):
        embed1=discord.Embed(title='',description='',color=0xb6b8ba)
        embed1.set_image(url=random.choice(jdata['LOLYPICTURE']))
        await ctx.channel.send(embed=embed1)
def setup(bot):
    bot.add_cog(Fun(bot))