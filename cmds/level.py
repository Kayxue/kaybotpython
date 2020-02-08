import discord
from discord.ext import commands
from core.classes import *
import json,os

class Level(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,message):
        with open("level.json",mode="r",encoding='utf8') as jfile:
            jdata=json.load(jfile)
        if os.path.isfile("level.json"):
            if message.author.id not in jdata:
                jdata[message.author.id] = {}
                jdata[message.author.id]['level'] = 1
                jdata[message.author.id]['xp'] = 1
                with open("level.json",mode="w",encoding='utf8')as finish:
                    json.dump(jdata,finish,sort_keys=True,indent=4)
            else:
                jdata[message.author.id]['xp'] += 1
                if jdata[message.author.id]['xp'] == int(jdata[message.author.id]['level'])*3:
                    jdata[message.author.id]['level'] += 1
                    jdata[message.author.id]['xp'] = 0
                    with open("level.json",mode="w")as finish:
                        json.dump(jdata,finish,sort_keys=True,indent=4)
                    await message.guild.channel.send(f"恭喜{message.author.mention}！您升到了等級{jdata[message.author.id]['level']}！")
                else:
                    with open("level.json",mode="w")as finish:
                        json.dump(jdata,finish,sort_keys=True,indent=4)
        else:
            users={message.author.id:{}}
            users[message.author.id]['level'] = 1
            with open("level.json",mode="w")as finish:
                json.dump(users,finish,sort_key=True,indent=4)

def setup(bot):
    bot.add_cog(Level(bot))