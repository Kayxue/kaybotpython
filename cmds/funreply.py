import discord
from discord.ext import commands
import json
import random
from core.classes import *

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class FunReply(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author != self.bot.user:
            if '晚安' in str(message.content):
                if '各位' in str(message.content):
                    await message.channel.send(f'晚安！{message.author.mention}！')
                else:
                    if message.channel.name == "和湯圓說說話":
                        await message.channel.send(f"{message.author.mention}：晚安")
                    else:
                        await message.channel.send(f'晚安！')
            elif '早安' in str(message.content):
                if '各位' in str(message.content):
                    await message.channel.send(f'早安！{message.author.mention}！')
                else:
                    if message.channel.name == "和湯圓說說話":
                        await message.channel.send(f"{message.author.mention}：早安")
                    else:
                        await message.channel.send(f'早安！')
            elif '嗨' in str(message.content) or 'Hi' in str(message.content):
                if message.channel.name == "和湯圓說說話":
                    await message.channel.send(f'{message.author.mention}：嗨')
                else:
                    await message.channel.send('嗨')
            elif str(message.channel.name) == "和湯圓說說話" :
                randommes=random.choice(jdata['RANDOMMESSAGE'])
                await message.channel.send(f"{message.author.mention}：{randommes}")
            
def setup(bot):
    bot.add_cog(FunReply(bot))