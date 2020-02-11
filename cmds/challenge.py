import discord
from discord.ext import commands
import json
from core.classes import *

class Challenge(Cog_Extension):
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def makechallenge(self,ctx,game:str,level:str,info:str,endtime:str):
        with open('count.json',mode='r',encoding='utf8') as jfile:
            jdata=json.load(jfile)
        with open('challenge.json',mode='r',encoding='utf8') as jfile:
            challenges=json.load(jfile)
        jdata['challengecount'] += 1
        channel=discord.utils.get(ctx.guild.channels,name="挑戰challenge")
        challenges[str(jdata['challengecount'])]={}
        challenges[str(jdata['challengecount'])]['game']=game
        challenges[str(jdata['challengecount'])]['level']=level
        challenges[str(jdata['challengecount'])]['info']=info
        challenges[str(jdata['challengecount'])]['endtime']=endtime
        challenges[str(jdata['challengecount'])]['status']="Starting"
        challenges[str(jdata['challengecount'])]['host']=ctx.author.id
        embed1=discord.Embed(title=f"挑戰#{jdata['challengecount']}",color=0xb6b8ba)
        embed1.add_field(name='挑戰遊戲：',value=game)
        embed1.add_field(name='挑戰關卡：',value=level)
        embed1.add_field(name='挑戰內容：',value=info)
        embed1.add_field(name='截止時間：',value=endtime)
        embed1.set_footer(text=ctx.author,icon_url=ctx.author.avatar_url)
        with open('count.json',mode='w',encoding='utf8') as finish:
            json.dump(jdata,finish,sort_keys=True,indent=4,ensure_ascii=False)
        outmsg = await channel.send(content=f"{(discord.utils.get(ctx.guild.roles,name='Event')).mention}挑戰已開始！",embed=embed1)
        challenges[str(jdata['challengecount'])]['messageid']=outmsg.id
        with open('challenge.json',mode='w',encoding='utf8') as finish:
            json.dump(challenges,finish,sort_keys=True,indent=4,ensure_ascii=False)
        await ctx.channel.send("挑戰已成功發布！")
    
    @makechallenge.error
    async def makechallenge_error(self,ctx,error):
        if isinstance(error,discord.ext.commands.CheckFailure):
            embed1=discord.Embed(title='權限不足！',description='您沒有權限執行此指令！',color=0xb6b6ba)
            embed1.add_field(name='請確認您是否有以下權限：',value='管理員')
            await ctx.channel.send(embed=embed1)
        elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
            embed1=discord.Embed(title='你少輸入某些資訊！',description='不會用嗎？沒關係，我幫你',color=0xb6b8ba)
            embed1.add_field(name='用法',value='``s!makechallenge [遊戲名稱] [挑戰關卡] [挑戰內容] [截止時間]``')
            embed1.add_field(name='範例',value='``s!makechallenge 滾動的天空 雷鬼 0石3冠 2100年7月8日``')
            await ctx.channel.send(embed=embed1)
        else:
            embed1=discord.Embed(title='輸出失敗！',description='對不起，無法執行！',color=0xb6b8ba)
            embed1.add_field(name='錯誤訊息：',value=error)
            await ctx.channel.send(embed=embed1)
            
    @commands.command()
    async def challengeinfo(self,ctx,chalid:str):
        try:
            with open('challenge.json',mode='r',encoding='utf8') as jfile:
                challenges=json.load(jfile)
            host=ctx.guild.get_member(int(challenges[chalid]['host']))
            embed1=discord.Embed(title=f'挑戰#{chalid}',color=0xb6b8ba)
            if challenges[chalid]['status']=="Starting":
                embed1.add_field(name="活動狀態",value="正在進行")
            elif challenges[chalid]['status']=="Ended":
                embed1.add_field(name="活動狀態",value="已結束")
            embed1.add_field(name="挑戰遊戲：",value=challenges[chalid]['game'])
            embed1.add_field(name="挑戰關卡：",value=challenges[chalid]['level'])
            embed1.add_field(name="挑戰內容：",value=challenges[chalid]['info'])
            embed1.add_field(name="截止時間：",value=challenges[chalid]['endtime'])
            embed1.add_field(name="舉辦者：",value=host.mention)
            await ctx.channel.send(embed=embed1)
        except KeyError:
            await ctx.channel.send("查無此挑戰喔！")
    
    @challengeinfo.error
    async def challengeinfo_error(self,ctx,error):
        if isinstance(error, discord.ext.commands.MissingRequiredArgument):
            embed1=discord.Embed(title='請輸入要查詢之挑戰編號！',description='不會用嗎？沒關係，我幫你',color=0xb6b8ba)
            embed1.add_field(name='用法',value='``s!challengeinfo [挑戰編號]``')
            embed1.add_field(name='範例',value='``s!challengeinfo 3``')
            await ctx.channel.send(embed=embed1)
        else:
            embed1=discord.Embed(title='輸出失敗！',description='對不起，無法執行！',color=0xb6b8ba)
            embed1.add_field(name='錯誤訊息：',value=error)
            await ctx.channel.send(embed=embed1)
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def endchallenge(self,ctx,chalid:str):
        try:
            with open('challenge.json',mode='r',encoding='utf8') as jfile:
                challenges=json.load(jfile)
            if challenges[chalid]['status']=="Starting":
                channel=discord.utils.get(ctx.guild.channels,name="挑戰challenge")
                host=ctx.guild.get_member(int(challenges[chalid]['host']))
                messagetoedit=await channel.fetch_message(int(challenges[chalid]['messageid']))
                challenges[chalid]['status']="Ended"
                with open('challenge.json',mode='w',encoding='utf8') as finish:
                    json.dump(challenges,finish,sort_keys=True,indent=4,ensure_ascii=False)
                embed1=discord.Embed(title=f'挑戰#{chalid}',color=0xff0000)
                embed1.add_field(name="挑戰遊戲：",value=challenges[chalid]['game'])
                embed1.add_field(name="挑戰關卡：",value=challenges[chalid]['level'])
                embed1.add_field(name="挑戰內容：",value=challenges[chalid]['info'])
                embed1.add_field(name="截止時間：",value=challenges[chalid]['endtime'])
                embed1.set_footer(text=host,icon_url=host.avatar_url)
                await messagetoedit.edit(content="挑戰已結束",embed=embed1)
                await ctx.channel.send("訊息已成功更改")
            else:
                await ctx.channel.send("該挑戰已經為結束狀態")
        except KeyError:
            await ctx.channel.send("查無此挑戰喔！")
            
    @endchallenge.error
    async def endchallenge_error(self,ctx,error):
        if isinstance(error,discord.ext.commands.CheckFailure):
            embed1=discord.Embed(title='權限不足！',description='您沒有權限執行此指令！',color=0xb6b6ba)
            embed1.add_field(name='請確認您是否有以下權限：',value='管理員')
            await ctx.channel.send(embed=embed1)
        elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
            embed1=discord.Embed(title='請輸入要結束之挑戰編號！',description='不會用嗎？沒關係，我幫你',color=0xb6b8ba)
            embed1.add_field(name='用法',value='``s!endchallenge [挑戰編號]``')
            embed1.add_field(name='範例',value='``s!endchallenge 3``')
            await ctx.channel.send(embed=embed1)
        else:
            embed1=discord.Embed(title='輸出失敗！',description='對不起，無法執行！',color=0xb6b8ba)
            embed1.add_field(name='錯誤訊息：',value=error)
            await ctx.channel.send(embed=embed1)

def setup(bot):
    bot.add_cog(Challenge(bot))
    