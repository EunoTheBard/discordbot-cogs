import discord
import asyncio
import urllib.request
import requests
from discord.ext import commands

class ShortenUrl:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    """
    Checks if the user matches the role required to process the command
    otherwise it returns "nope".
    
    We use the comman ouo as we are using the ouo webapp to process the
    shortening of the url.
    """
    async def ouo(self, ctx):
        if "465896415751569408" in [role.id for role in ctx.message.author.roles]:
            url = ("http://ouo.io/api/B3Nm9g8L?s=" + ctx.message.content)
            handle = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            html = urllib.request.urlopen(handle).read().decode('utf-8')
            await self.bot.say("Shortened: " + html)
            await asyncio.sleep(1)
        else:
            await self.bot.say("nope")
            await asyncio.sleep(1)

def setup(bot):
    bot.add_cog(ShortenUrl(bot))
