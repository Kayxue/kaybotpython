import discord
from discord.ext import commands
from core.classes import *
import json,time

with open("level.json",mode="r",encoding='utf8') as jfile:
    jdata=json.load(jfile)

class Level(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,message):
        userid=str(message.author.id)
        if not message.author.bot :
            if str(userid) not in jdata:
                jdata[userid] = {}
                jdata[userid]['level'] = 1
                jdata[userid]['xp'] = 1
                jdata[userid]['coin']=1
                jdata[userid]['challengepass']=0
                with open("level.json",mode="w",encoding='utf8')as finish:
                    json.dump(jdata,finish,sort_keys=True,indent=4)
            else:
                jdata[userid]['xp'] += 1
                if int(jdata[userid]['xp']) == int(jdata[userid]['level'])*3:
                    jdata[userid]['level'] += 1
                    jdata[userid]['xp'] = 0
                    jdata[userid]['coin'] += jdata[userid]['level']
                    with open("level.json",mode="w")as finish:
                        json.dump(jdata,finish,sort_keys=True,indent=4)
                    await message.channel.send(f"恭喜{message.author.mention}！您升到了等級{jdata[userid]['level']}！")
                else:
                    with open("level.json",mode="w")as finish:
                        json.dump(jdata,finish,sort_keys=True,indent=4)

def setup(bot):
    bot.add_cog(Level(bot))