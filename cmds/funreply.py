from discord.ext import commands
import json
import random

with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class FunReply(commands.Cog):
    def __init__(self, bot):
        self.gamequestion = False
        self.normalquestion = False
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if message.author != self.bot.user:
                if "晚安" in str(message.content):
                    if "各位" in str(message.content):
                        await message.channel.send(f"晚安！{message.author.mention}！")
                    else:
                        if message.channel.name == "和湯圓說說話":
                            if self.gamequestion is True or self.normalquestion is True:
                                self.gamequestion = False
                                self.normalquestion = False
                            await message.channel.send(
                                f"{message.author.mention}：晚安"
                            )
                        else:
                            await message.channel.send("晚安！")
                elif "早安" in str(message.content):
                    if "各位" in str(message.content):
                        await message.channel.send(f"早安！{message.author.mention}！")
                    else:
                        if message.channel.name == "和湯圓說說話":
                            if self.gamequestion is True or self.normalquestion is True:
                                self.gamequestion = False
                                self.normalquestion = False
                            await message.channel.send(
                                f"{message.author.mention}：早安"
                            )
                        else:
                            await message.channel.send("早安！")
                elif "嗨" in str(message.content) or "Hi" in str(message.content):
                    if message.channel.name == "和湯圓說說話":
                        if self.gamequestion is True or self.normalquestion is True:
                            self.gamequestion = False
                            self.normalquestion = False
                        await message.channel.send(f"{message.author.mention}：嗨")
                    else:
                        await message.channel.send("嗨")
                elif str(message.channel.name) == "和湯圓說說話":
                    if not (message.content.startswith("s!")):
                        if self.gamequestion is False and self.normalquestion is False:
                            typeout = random.choice(jdata["QUESTIONORMESSAGE"])
                            if typeout == "QUESTIONNORMAL":
                                self.normalquestion = True
                                self.gamequestion = False
                                outputmsg = random.choice(jdata[f"{typeout}"])
                                await message.channel.send(
                                    f"{message.author.mention}：{outputmsg}"
                                )
                            elif typeout == "QUESTIONGAME":
                                self.gamequestion = True
                                self.normalquestion = False
                                outputmsg = random.choice(jdata[f"{typeout}"])
                                await message.channel.send(
                                    f"{message.author.mention}：{outputmsg}"
                                )
                            elif typeout == "RANDOMMESSAGE":
                                self.gamequestion = False
                                self.normalquestion = False
                                outputmsg = random.choice(jdata[f"{typeout}"])
                                await message.channel.send(
                                    f"{message.author.mention}：{outputmsg}"
                                )
                        elif self.gamequestion is True and self.normalquestion is False:
                            self.gamequestion = False
                            self.normalquestion = False
                            outputmsg = random.choice(jdata["ANSWERGAME"])
                            await message.channel.send(
                                f"{message.author.mention}：{outputmsg}"
                            )
                        elif self.gamequestion is False and self.normalquestion is True:
                            self.gamequestion = False
                            self.normalquestion = False
                            outputmsg = random.choice(jdata["ANSWERNORMAL"])
                            await message.channel.send(
                                f"{message.author.mention}：{outputmsg}"
                            )

    @commands.command()
    async def debugevent(self, ctx):
        await ctx.channel.send(f"是否正回答遊戲問題：{self.gamequestion}")
        await ctx.channel.send(f"是否正回答一般問題：{self.normalquestion}")


def setup(bot):
    bot.add_cog(FunReply(bot))
