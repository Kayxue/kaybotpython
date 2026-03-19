import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name="歡迎welcome")
        embed1 = discord.Embed(
            title="歡迎新成員！",
            description=f"歡迎{member.mention}來到此伺服器！",
            color=0xB6B8BA,
        )
        embed1.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed1)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.channels, name="歡迎welcome")
        embed2 = discord.Embed(
            title="向成員說再見！",
            description=f"{member}離開了此伺服器，再見！{member}！",
            color=0xB6B8BA,
        )
        embed2.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed2)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        channel = discord.utils.get(before.guild.channels, name="sesame-log")
        embed1 = discord.Embed(
            title="訊息已編輯", description="有使用者編輯了他的訊息", color=0xB6B8BA
        )
        embed1.add_field(
            name="發訊息之使用者：", value=f"{before.author.mention}", inline=False
        )
        embed1.add_field(name="於頻道：", value=f"<#{before.channel.id}>", inline=False)
        embed1.add_field(
            name="修改前文字訊息：", value=f"{before.content}", inline=True
        )
        embed1.add_field(name="修改後文字訊息：", value=f"{after.content}", inline=True)
        embed1.add_field(name="修改前嵌入式訊息：", value=before.embeds, inline=False)
        embed1.add_field(name="修改後嵌入式訊息：", value=after.embeds, inline=True)
        embed1.set_thumbnail(url=before.author.avatar_url)
        embed1.set_footer(text=before.author, icon_url=before.author.avatar_url)
        await channel.send(embed=embed1)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = discord.utils.get(message.guild.channels, name="sesame-log")
        embed1 = discord.Embed(
            title="訊息已刪除", description="有使用者的訊息被刪除", color=0xB6B8BA
        )
        embed1.add_field(
            name="發訊息之使用者：", value=f"{message.author.mention}", inline=False
        )
        embed1.add_field(
            name="於頻道：", value=f"<#{message.channel.id}>", inline=False
        )
        embed1.add_field(name="訊息內容：", value=f"{message.content}", inline=False)
        embed1.set_thumbnail(url=message.author.avatar_url)
        embed1.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await channel.send(embed=embed1)


def setup(bot):
    bot.add_cog(Event(bot))
