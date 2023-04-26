from discord.ext import commands

class CLASSNAME(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def COMMAND1(self, ctx):
        #Code command here
        await ctx.send("TEXT FOR BOT TO SEND")
       
    
async def setup(bot):
    await bot.add_cog(CLASSNAME(bot))