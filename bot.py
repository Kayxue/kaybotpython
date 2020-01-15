import discord
import youtube_dl
from discord.ext import commands
import random

bot=commands.Bot(command_prefix='s!')
client=discord.Client()

@bot.event
async def on_ready():
    print('Bot is online')

@bot.event
async def on_member_join(member):
    channel=discord.utils.get(member.guild.channels,name="歡迎welcome")
    embed1=discord.Embed(title='歡迎新成員！',description=f'歡迎{member.mention}來到此伺服器！',color=0xffffff)
    embed1.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed1)
@bot.event
async def on_member_remove(member):
    channel=discord.utils.get(member.guild.channels,name="歡迎welcome")
    embed2=discord.Embed(title='向成員說再見！',description=f'{member}離開了此伺服器，再見！{member}！',color=0xffffff)
    embed2.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed2)

@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice
    await bot.join_voice_channel(channel)

@bot.command()
async def leave(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()

@bot.command()
async def clear(ctx,amount=100):
    channel=ctx.message.channel
    messages=[]
    async for message in bot.logs_from(channel, limit=int(amount)+1):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say(f'刪除訊息完成！')
bot.run('NjE2OTQwOTQ4NDkxODYyMDI4.XeN__A.1r7oAV6hK0QCRwgeJPHB_VM1ApE')
