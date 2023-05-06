import discord
import os
import games
from dotenv import load_dotenv
from epicstore_api import EpicGamesStoreAPI, OfferData
from datetime import datetime

# Load evniroment variables.
load_dotenv()
    
def run_discord_bot():

    # Bot permissions.
    intents = discord.Intents.default()
    intents.message_content = True   
    client = discord.Client(intents=intents)

    # Info when bot is ready.
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    # Send list of games on command.
    @client.event   
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content.__eq__('test'):
            await message.channel.send(games.main())

    client.run(os.getenv('TOKEN'))
