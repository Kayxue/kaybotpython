import discord
from discord.ext import commands
from core.classes import *

class ServerInfo(Cog_Extension):
    @commands.command()
    async def serverinfo(self,ctx):
        membercounts={"botcount":0,
                      "membercount":0}
        statuses={"online":0,
                  "donotdisturb":0,
                  "idle":0,
                  "offline":0}
        channel={"category":len(ctx.guild.categories),
                 "textchannel":len(ctx.guild.channels)-len(ctx.guild.voice_channels),
                 "voicechannel":len(ctx.guild.voice_channels)}
        safety={"2fa level":ctx.guild.mfa_level,"verification level":ctx.guild.verification_level}
        region=ctx.guild.region

        '''計算機器人與使用者數量'''
        for mem in ctx.guild.members:
            if mem.bot:
                membercounts['botcount'] += 1
            else:
                membercounts['membercount'] += 1

        '''計算各使用者與機器人之狀態'''
        for mem in ctx.guild.members:
            if str(mem.status) == "online":
                statuses['online'] += 1
            elif str(mem.status) == "idle":
                statuses['idle'] += 1
            elif str(mem.status) == "dnd":
                statuses['donotdisturb'] += 1
            elif str(mem.status) == "offline":
                statuses['offline'] += 1

        '''驗證層級轉換'''
        if safety['verification level'] == discord.VerificationLevel.none:
            safety['verification level'] = "無設定"
        elif safety['verification level'] == discord.VerificationLevel.low:
            safety['verification level'] = "低驗證層級"
        elif safety['verification level'] == discord.VerificationLevel.medium:
            safety['verification level'] = "中驗證層級"
        elif safety['verification level'] == discord.VerificationLevel.high or safety['verification level'] == discord.VerificationLevel.table_flip:
            safety['verification level'] = "高驗證層級"
        elif safety['verification level'] == discord.VerificationLevel.extreme or safety['verification level'] == discord.VerificationLevel.double_table_flip:
            safety['verification level'] = "最高驗證層級"

        '''是否啟用2FA'''
        if safety['2fa level'] == 1:
            safety['2fa level'] = '是'
        elif safety['2fa level'] == 0:
            safety['2fa level'] = '否'

        '''轉換地區'''
        if region == discord.VoiceRegion.amsterdam:
            region = "荷蘭阿姆斯特丹"
        elif region == discord.VoiceRegion.brazil:
            region = "巴西"
        elif region == discord.VoiceRegion.dubai:
            region = "杜拜"
        elif region == discord.VoiceRegion.eu_central:
            region = "中歐"
        elif region == discord.VoiceRegion.eu_west:
            region = "西歐"
        elif region == discord.VoiceRegion.europe:
            region = "歐洲"
        elif region == discord.VoiceRegion.frankfurt:
            region = "德國法蘭克福"
        elif region == discord.VoiceRegion.hongkong:
            region = "香港"
        elif region == discord.VoiceRegion.india:
            region = "印度"
        elif region == discord.VoiceRegion.japan:
            region = "日本"
        elif region == discord.VoiceRegion.london:
            region = "英國倫敦"
        elif region == discord.VoiceRegion.russia:
            region = "俄羅斯"
        elif region == discord.VoiceRegion.singapore:
            region = "新加坡"
        elif region == discord.VoiceRegion.southafrica:
            region = "南非"
        elif region == discord.VoiceRegion.sydney:
            region = "澳洲雪梨"
        elif region == discord.VoiceRegion.us_central:
            region = "美國中部"
        elif region == discord.VoiceRegion.us_east:
            region = "美國東部"
        elif region == discord.VoiceRegion.us_south:
            region = "美國南部"
        elif region == discord.VoiceRegion.us_west:
            region = "美國西部"
        
        '''輸出嵌入式訊息'''
        embed1=discord.Embed(title=f"關於伺服器「{ctx.guild.name}」",description=f"關於伺服器{ctx.guild.name}的資訊",color=0xb6b8ba)
        embed1.add_field(name="伺服器ID",value=f"{ctx.guild.id}",inline=False)
        embed1.add_field(name=f"成員［{ctx.guild.member_count}］：",value=f"使用者人數：{membercounts['membercount']}\n機器人個數：{membercounts['botcount']}\n上線人數：{statuses['online']}\n閒置狀態人數：{statuses['idle']}\n勿擾狀態人數：{statuses['donotdisturb']}\n離線人數：{statuses['offline']}",inline=True)
        embed1.add_field(name=f"頻道［{len(ctx.guild.channels)}］：",value=f"頻道類別數量：{channel['category']}\n文字頻道數量：{channel['textchannel']}\n語音頻道數量：{channel['voicechannel']}",inline=True)
        embed1.add_field(name="安全層級",value=f"驗證等級：{safety['verification level']}\n兩步驟驗證是否啟用：{safety['2fa level']}",inline=True)
        embed1.add_field(name="伺服器地區",value=f"{region}",inline=True)
        embed1.add_field(name="服主",value=f"{ctx.guild.owner.mention}")
        embed1.set_thumbnail(url=ctx.guild.icon_url)
        embed1.set_footer(text=ctx.author,icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed1)
        
    @commands.command()
    async def serverboost(self,ctx):
        embed1=discord.Embed(title=f"關於伺服器{ctx.guild.name}之加成資料",description="關於此伺服器現在之加成資料",color=0xb6b8ba)
        premiums={"level":ctx.guild.premium_tier,"boost user count":ctx.guild.premium_subscription_count}
        if premiums['boost user count'] == 0:
            premiums['boost user count'] = "無人加成" 
        embed1.add_field(name="此伺服器加成等級：",value=premiums['level'])
        embed1.add_field(name="此伺服器加成人數",value=premiums['boost user count'])
        await ctx.channel.send(embed=embed1)

def setup(bot):
    bot.add_cog(ServerInfo(bot))