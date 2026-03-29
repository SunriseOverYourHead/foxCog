from .foxcog import FoxCog

async def setup(bot):
    await bot.add_cog(FoxCog(bot))