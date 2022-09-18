from nextcord.ui import View, Select
from nextcord import Interaction
import nextcord


class SelectProblemSelect(Select):
    def __init__(self):
        super().__init__(
            placeholder="The problem is...",
            min_values=1,
            max_values=1,
            options=[
                nextcord.SelectOption(label="with Discord", value="0"),
                nextcord.SelectOption(label="with python", value="1"),
                nextcord.SelectOption(label="an event or command not working", value="2"),
                nextcord.SelectOption(label="a general bug (in code)", value="3"),
                nextcord.SelectOption(label="not here", value="4"),
            ]
        )

    async def callback(self, interaction: Interaction) -> None:
        if self.values[0] == "0":
            return await interaction.response.send_message(
                embed=nextcord.Embed(title="The problem is with discord", url="")
            )

        elif self.values[0] == "1":
            return await interaction.response.send_message(
                embed=nextcord.Embed(title="The problem is with python", url="")
            )

        elif self.values[0] == "2":
            return await interaction.response.send_message(
                embed=nextcord.Embed(title="The problem is an event or command", url="")
            )

        elif self.values[0] == "3":
            return await interaction.response.send_message(
                embed=nextcord.Embed(title="The problem is a general bug", url="")
            )

        elif self.values[0] == "4":
            return await interaction.response.send_message(
                embed=nextcord.Embed(title="The problem is something else", url="")
            )


class SelectProblemView(View):
    def __init__(self):
        super(SelectProblemView, self).__init__()

        self.add_item(SelectProblemSelect())
