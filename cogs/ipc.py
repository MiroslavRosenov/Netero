from discord.ext import commands, ipc


class IpcRoutes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @ipc.server.route()
    async def get_guild_count(self, data):
        return len(self.guilds)

    @ipc.server.route()
    async def get_guild_ids(self, data):
        final = []
        for guild in self.guilds:
            final.append(guild.id)
        return final  # returns the guild ids to the client


async def setup(bot):
    bot.add_cog(IpcRoutes(bot))
