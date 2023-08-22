import discord
import os
import games
from dotenv import load_dotenv
from epicstore_api import EpicGamesStoreAPI, OfferData
import datetime
from discord.ext import tasks

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
        if not remind.is_running():
            remind.start() # If the task is not already running, start it.
            print("Reminder task started!")

    # Send list of games on command.
    @client.event   
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content.__eq__('games'):
            await message.channel.send(f'{role}\n{free_games}')

    # Send list of games at specific time
    @tasks.loop(hours=72)
    async def remind():
        await client.wait_until_ready()
        channel = client.get_channel(1143101326943850577) # doesn't work off .env file
        await channel.send(f'{role}\n{free_games}')


    client.run(os.getenv('TOKEN'))