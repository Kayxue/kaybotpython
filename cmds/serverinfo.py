import discord
from discord.ext import commands
from core.classes import *

class ServerInfo(Cog_Extension):
    @commands.command()
    async def serverinfo(self,ctx):
        botcount=0
        membercount=0
        onlines=0
        donotdisturbs=0
        idles=0
        offlines=0
        voicechannel=len(ctx.guild.voice_channels)
        textchannel=len(ctx.guild.channels)-len(ctx.guild.voice_channels)
        categorys=len(ctx.guild.categories)
        for mem in ctx.guild.members:
            if mem.bot:
                botcount += 1
            else:
                membercount += 1
        for mem in ctx.guild.members:
            if str(mem.status) == "online":
                onlines += 1
            elif str(mem.status) == "idle":
                idles += 1
            elif str(mem.status) == "dnd":
                donotdisturbs += 1
            elif str(mem.status) == "offline":
                offlines += 1
        embed1=discord.Embed(title=f"關於伺服器「{ctx.guild.name}」",description=f"關於伺服器{ctx.guild.name}的資訊")
        embed1.add_field(name="伺服器ID",value=f"{ctx.guild.id}",inline=False)
        embed1.add_field(name=f"成員［{ctx.guild.member_count}］：",value=f"使用者人數：{membercount}\n機器人個數：{botcount}\n上線人數：{onlines}\n閒置狀態人數：{idles}\n勿擾狀態人數：{donotdisturbs}\n離線人數：{offlines}",inline=True)
        embed1.add_field(name=f"頻道［{len(ctx.guild.channels)}］：",value=f"頻道類別數量：{categorys}\n文字頻道數量：{textchannel}\n語音頻道數量：{voicechannel}",inline=True)
        await ctx.channel.send(embed=embed1)

def setup(bot):
    bot.add_cog(ServerInfo(bot))