import os # Used to load the token environment variable
import disnake # Used for discord bot functionality
from disnake.ext import commands
from dotenv import load_dotenv # Used to load .env files

# Load the discord bot token
load_dotenv("token.env")
TOKEN = os.getenv('BOT_TOKEN')

