# tis is the main file for the project,
#! So Don't Mess this up

#? ......................[imports]...........................
# Build-in modules
import os
from pathlib import Path

# Nextcord Module
import nextcord
from nextcord.ext import commands

# .ENV
from dotenv import load_dotenv

#* Loading all the Variables from the .env file
env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

#? ......................[variables]..........................
#* Tokens
_TOKEN = str(os.getenv('DiscordBotToken'))  # <- Discord Bot Token

#* Admin IDs
_adminUserID = [557756298838409226, 827181645672480798]   # <- IDs of Admin Users
_adminGuildID = [1014583421604991106]  # <- ID of Admin Guild (Server)


#?  ......................[client init]......................
# Bot initialzation
intents = nextcord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='eb!', intents=intents)

# to remove the default Help command
client.remove_command("help")


print(f'''
-------------------------------------------------------------------
Loading COGs....
-------------------------------------------------------------------
''')

#? ----------------------[all loader]-------------------------
# load all the cog file ends with .py from ./cogs
for folder in os.listdir("./src/cogs"):
    for file in os.listdir(f"./src/cogs/{folder}"):
        if file.endswith(".py"):
            try:
                client.load_extension(f"cogs.{folder}.{file[:-3]}") # <- load extension and remove .py from extension file>
                print(f"    {file[:-3]} Loaded")
            except:
                print(f"    {file[:-3]} error")


#? ......................[on_ready event].....................
@client.event
async def on_ready():
    print(f'''
-------------------------------------------------------------------
Success!!
-------------------------------------------------------------------

Stats:-
    Appication ID   : {client.user.id}
    Appication name : {client.user}
    State           : Online
    Ping            : {round(client.latency * 1000)}

-------------------------------------------------------------------
''')

#? ......................[main-code]..........................
# test cmd
@client.command()
async def status(ctx):
    await ctx.send(f"I'm alive, \nand logged in as '{client.user}', \nPing: {round(client.latency * 1000)}")


#? ......................[run function].......................
if __name__ == '__main__':
    client.run(_TOKEN)
