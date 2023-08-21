import discord
import os
import games
from dotenv import load_dotenv
from epicstore_api import EpicGamesStoreAPI, OfferData
from datetime import datetime, time

# Load evniroment variables.
load_dotenv()

def run_discord_bot():

    # Bot permissions.
    intents = discord.Intents.default()
    intents.message_content = True   
    client = discord.Client(intents=intents)
    channel = client.get_channel(os.getenv('CHANNEL'))
    role = '<@&1101520722670661733>' # doesn't work off .env file
    free_games = '\n'.join(games.main())

    # Info when bot is ready.
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    # Send list of games on command.
    @client.event   
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content.__eq__('games'):
            await message.channel.send(f'{role}\n{free_games}')

    client.run(os.getenv('TOKEN'))