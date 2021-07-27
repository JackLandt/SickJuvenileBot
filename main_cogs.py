from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!')

class Test(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command():
    async def ping(self, ctx):
      await ctx.send('Pong')

bot.add_cog(Test(bot))

bot.run('ODY1NjMyOTY1ODkxNzE5MjA5.YPG1hQ.DDCgzgtjjF5PuDzQkwGeWH4s0EA')