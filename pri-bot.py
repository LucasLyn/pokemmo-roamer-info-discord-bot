import os # Used to load the token environment variable
import sys # Used to insert the sys path at runtime
from copy import deepcopy # Used to copy objects that need to be modified
import importlib # Used to import unconventinally named submodules 
import disnake # Used for discord bot functionality
from disnake.ext import commands
from dotenv import load_dotenv # Used to load .env files

# Set sys path to pokemmo-roamer-info to properly import in submodule
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pokemmo-roamer-info'))

# Dirty pokemmo-roamer-info submodule imports
# Could be fixed by using '_' instead of '-' in submodule name
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

bot = commands.InteractionBot()


@bot.event # Report successful login in console
async def on_ready():
    print(f'Successfully logged in as {bot.user.name} ({bot.user.id})')


def find_matching_emoji(name:str, guild:disnake.Guild) -> disnake.emoji.Emoji:
    '''
    Finds an emoji in a given guild with a name matching that of 'name'.

    ### Parameters:
    - name (str):
        The name of the emoji to find.
    
    - guild (disnake.Guild):
        The guild to check emoji's from.

    ### Returns:
        An emoji object with the matching name if one was found. None otherwise.
    '''
    return disnake.utils.get(guild.emojis, name=name)


def prepend_emoji_to_roamer(roamer, emoji:disnake.emoji.Emoji):
    '''
    Prepends an emoji to the name of a roamer.

    ### Parameters:
    - roamer (Roamer):
        The roamer to prepend the moji to.
    
    - emoji (disnake.emoji.Emoji):
        The emoji to prepend.
    
    ### Returns:
        A Roamer object with an emoji prepended to its name.
    '''
    if emoji != None:
        roamer.name = f"{emoji} {roamer.name}"
    return roamer


def prepend_matching_emojis_to_all_roamers(roamers, guild):
    '''
    Find any matching emojis and prepend them to the name of each roamer.
    Wrapper for the functions 'find_matching_emoji()' and 'prepend_emoji_to_roamer()'.

    ### Parameters:
    - roamers (list[Roamer]):
        The list of roamers to prepend their matching emoji to.
    
    - guild (disnake.Guild):
        The guild to search emojis from.
    
    ### Returns:
        A roamer list where all roamers have their name prepended by any found matching emojis.
    '''
    for roamer in roamers:
        if roamer == None:
            continue
        emoji = find_matching_emoji(roamer.name.lower(), guild)
        roamer = prepend_emoji_to_roamer(roamer, emoji)
    
    return roamers


# Get the active roamers in a given month
@bot.slash_command(name="roamers",
                   description="Get the currently active roamers in each region")
async def roamers(ctx,
                  month:int = current_month,
                  show_next_roamers:bool = True):
    curr_guild = ctx.guild

    # Ensure given month is within bounds
    if month != current_month:
        month = month if month in range(1, 12) else 1 if month < 1 else 12

    # Set current and next month values and names
    month_name = month_names[month]
    next_month = month+1 if month < 12 else 1
    next_month_name = month_names[next_month]

    # Set roamers in current month string
    curr_roamers = deepcopy(get_avail_roamers_in_month(all_roamers, month))
    curr_roamers = prepend_matching_emojis_to_all_roamers(curr_roamers, curr_guild)
    curr_roamers_str = get_avail_roamers_str(curr_roamers,
                                             prefix_str=f"Currently available roamers ({month_name})")

    # Set roamers in next month string
    next_roamers_str = '' # init empty to avoid problems with .join()
    if show_next_roamers:
        next_roamers = deepcopy(get_avail_roamers_in_month(all_roamers, next_month))
        next_roamers = prepend_matching_emojis_to_all_roamers(next_roamers, curr_guild)
        next_roamers_str = get_avail_roamers_str(next_roamers,
                                                 prefix_str=f"Next available roamers ({next_month_name})")
    
    
    # Send the message
    await ctx.send(''.join([curr_roamers_str, next_roamers_str]))


bot.run(TOKEN)