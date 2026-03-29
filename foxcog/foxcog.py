import aiohttp
from redbot.core import commands

class FoxCog(commands.Cog):
    """Sends random foppy pictures"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fox(self, ctx):
        """Sends a random picture from randomfox.ca"""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://randomfox.ca/floof/") as response:
                if response.status == 200:
                    data = await response.json()
                    await ctx.send(data["image"])
                else:
                    await ctx.send("Couldn't fetch a fox right now :c Try again later!")