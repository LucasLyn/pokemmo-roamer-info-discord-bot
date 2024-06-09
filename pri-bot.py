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



# Load the discord bot token and init bot
load_dotenv("token.env")
TOKEN = os.getenv('BOT_TOKEN')

bot = commands.Bot()


@bot.event # Report successful login in console
async def on_ready():
    print(f'Successfully logged in as {bot.user.name} ({bot.user.id})')


# 
@bot.slash_command(name="roamers",
                   description="Get the currently active roamers in each region")
async def roamers(ctx,
                  month:int = current_month,
                  show_next_roamers:bool = True):
    # Ensure given month is within bounds
    if month != current_month:
        month = month if month in range(1, 12) else 1 if month < 1 else 12

    # Set current and next month values and names
    month_name = month_names[month]
    next_month = month+1 if month < 12 else 1
    next_month_name = month_names[next_month]

    # Set roamers in current month string
    curr_roamers = get_avail_roamers_in_month(all_roamers, month)
    curr_roamers_str = get_avail_roamers_str(curr_roamers, prefix_str=f"Currently available roamers ({month_name})")

    # Set roamers in next month string
    next_roamers_str = '' # init empty to void problems with .join()
    if show_next_roamers:
        next_roamers = get_avail_roamers_in_month(all_roamers, next_month)
        next_roamers_str = get_avail_roamers_str(next_roamers, prefix_str=f"Next available roamers ({next_month_name})")
    
    
    # Send the message
    await ctx.send(''.join([curr_roamers_str, next_roamers_str]))


bot.run(TOKEN)