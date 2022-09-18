from src.cogs.utils.ui import SelectProblemView
from nextcord.ext import commands
import nextcord


guild_ids: list[int] = [802568457031778324, 802568457031778324]


class GetSolutionCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=guild_ids)
    async def gethelp(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(view=SelectProblemView())


def setup(bot):
    bot.add_cog(GetSolutionCog(bot))
