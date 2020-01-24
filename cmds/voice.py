import discord
from discord.ext import commands
from core.classes import *

class Voice(Cog_Extension):
    
    @commands.command()
    async def join(self,ctx):
        
        await bot.connect()
    
    @commands.command()
    async def leave(self,ctx):
        server = ctx.message.server
        voice_client = self.bot.voice_client_in(server)
        await voice_client.disconnect()   
     
def setup(bot):
    bot.add_cog(Voice(bot))