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
    async def loli(self,ctx):
        embed1=discord.Embed(title='',description='',color=0xb6b8ba)
        embed1.set_image(url=random.choice(jdata['LOLYPICTURE']))
        await ctx.channel.send(embed=embed1)
    
    @commands.command()
    async def maketeam(self,ctx,howmanyinateam:int = 0,team:int = 0):
        if howmanyinateam >= 2:
            servermember=ctx.guild.members
            teamok=True
            onlines=[]
            outputstr=""
            teams={}
            dotimes=0
            i=0
            for mem in servermember:
                if str(mem.status) == 'online':
                    if not mem.bot:
                        onlines.append(mem)
            
            if team == 0:
                dotimes=int(len(onlines) / howmanyinateam)
            else:
                if not team > int(len(onlines) / howmanyinateam):
                    dotimes=team
                else:
                    await ctx.channel.send("無法分出指定隊數！")
                    teamok=True
            
            if not dotimes < 1:
                while i<dotimes:
                    listtitle=f"第{i+1}小隊成員："
                    teams[listtitle]=[]
                    j=1
                    while j<=howmanyinateam:
                        memb=random.choice(onlines)
                        teams[listtitle].append(memb)
                        delindex=onlines.index(memb)
                        del onlines[delindex]
                        j += 1
                    i += 1
            
                l=0
                embed1=discord.Embed(title="組隊結果",description="以下為組隊結果",color=0xb6b8ba)
                
                while l<dotimes:
                    outtitle=f"第{l+1}小隊成員："
                    outvalue=""
                    for mem in teams[outtitle]:
                        outvalue += f"{mem}\n"
                    embed1.add_field(name=outtitle,value=f"{outvalue}",inline=False)
                    l += 1
                
                await ctx.channel.send(embed=embed1)  
            elif dotimes < 1 and teamok == True :
                await ctx.channel.send(f"上線人數過少，無法分出{team}組並且一組{howmanyinateam}人")
            elif dotimes < 1 and teamok == False:
                await ctx.channel.send(f"上線人數過少，無法分出一組{howmanyinateam}人")
            
        else:
            await ctx.channel.send(f'請輸入一隊有幾人（此數字必須大於等於2）')
            
def setup(bot):
    bot.add_cog(Fun(bot))