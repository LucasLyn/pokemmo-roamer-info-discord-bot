import os # Used to load the token environment variable
import sys # Used to insert the sys path at runtime
import importlib # Used to import unconventinally named submodules 
import disnake # Used for discord bot functionality
from disnake.ext import commands
from dotenv import load_dotenv # Used to load .env files

# Set sys path to pokemmo-roamer-info to properly import in submodule
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pokemmo-roamer-info'))

# Dirty pokemmo-roamer-info submodule imports
init_module = importlib.import_module("pokemmo-roamer-info.__init__")
pri_module = importlib.import_module("pokemmo-roamer-info.pri")

current_month = getattr(init_module, "current_month")
month_names = getattr(init_module, "month_names")

get_avail_roamers_in_month = getattr(pri_module, "get_avail_roamers_in_month")
get_avail_roamers_str = getattr(pri_module, "get_avail_roamers_str")
all_roamers = getattr(pri_module, "all_roamers")



# Load the discord bot token
load_dotenv("token.env")
TOKEN = os.getenv('BOT_TOKEN')

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'Successfully logged in as {bot.user.name} ({bot.user.id})')



bot.run(TOKEN)