import discord
from discord.ext import commands
from core.classes import *

class Invite(Cog_Extension):
    @commands.command()
    async def createinvite(self,ctx,max_ages:int = 0,max_use:int = 0):
        invite = await ctx.message.channel.create_invite(reason=None,max_age=max_ages,max_uses=max_use)
        embed1=discord.Embed(title="成功建立此伺服器之邀請！",description=f"邀請連結如下：\n{invite.url}",color=0xb6b8ba)
        invites={"maxage":invite.max_age,"maxuse":invite.max_uses}
        if invites["maxage"] == 0:
            invites["maxage"] = "永久"
        if invites["maxuse"] == 0:
            invites["maxuse"] = "無限制"
        embed1.add_field(name="邀請有效時長：",value=f"{invites['maxage']}（秒）")
        embed1.add_field(name="邀請最大使用次數：",value=invites["maxuse"])
        await ctx.channel.send(embed=embed1)
    @commands.command()
    async def listinvite(self,ctx):
        channels=ctx.guild.channels
        invites=""
        invite=await ctx.guild.invites()
        for i in invite:
            invites += f"連結：{i.url}\n"
            invites += f"創造時間：{i.created_at}\n"
            invites += f"已使用次數：{i.uses}\n"
            invites += f"最大使用次數：{i.max_uses}\n"
            invites += f"建立於頻道：<#{i.channel.id}>\n"
            invites += f"建立人：{i.inviter.mention}\n"
            invites += ("-"*20) + "\n"
        embed1=discord.Embed(title="以下為此伺服器建立之邀請",description=f"{invites}",color=0xb6b8ba)
        await ctx.channel.send(embed=embed1)

def setup(bot):
    bot.add_cog(Invite(bot))