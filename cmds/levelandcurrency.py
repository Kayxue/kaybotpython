import discord
from discord.ext import commands
import json
from core.classes import *

class LevelAndCurrency(Cog_Extension):
    @commands.command()
    async def rank(self,ctx,mem:discord.Member=None):
        with open('level.json',mode='r',encoding='utf8') as jfile:
            datas=json.load(jfile)
        if mem == None:
            try:
                embed1=discord.Embed(title="您的等級卡",description=f"{ctx.author.name}的等級卡",color=0xb6b8ba)
                embed1.add_field(name="目前等級",value=f"{datas[str(ctx.author.id)]['level']}")
                embed1.add_field(name="目前XP",value=f"{int(datas[str(ctx.author.id)]['xp'])}/{int(datas[str(ctx.author.id)]['level'])*3}")
                embed1.add_field(name="目前擁有之金幣：",value=f"{datas[str(ctx.author.id)]['coin']}")
                await ctx.channel.send(embed=embed1)
            except KeyError:
                await ctx.channel.send("請先聊天喔！")
        else:
            if not mem.bot:
                try:
                    embed1=discord.Embed(title=f"使用者「{mem}」的資訊卡",description="您正在查看別人的等級卡喔！",color=0xb6b8ba)
                    embed1.add_field(name="目前等級",value=f"{datas[str(mem.id)]['level']}")
                    embed1.add_field(name="目前XP",value=f"{datas[str(mem.id)]['xp']}/{int(datas[str(mem.id)]['level'])*3}")
                    embed1.add_field(name="目前擁有之金幣：",value=f"{datas[str(mem.id)]['coin']}")
                    await ctx.channel.send(embed=embed1)
                except KeyError:
                    await ctx.channel.send("您指定之使用者尚未產生等級資料喔！")
            else:
                await ctx.channel.send("機器人沒有等級卡喔！")
                
def setup(bot):
    bot.add_cog(LevelAndCurrency(bot))