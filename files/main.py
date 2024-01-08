import os
import discord
import mcstatus
from discord.ext import tasks

TOKEN = os.environ['BOT_TOKEN']
IP_ADDRESS = os.environ['IP']

# Set up the necessary intents
intents = discord.Intents.default()
intents.messages = True  # If you need to handle messages, set this to True

client = discord.Client(intents=intents)

def get_server_status():
    try:
        server = mcstatus.lookup(IP_ADDRESS)
        status = server.status()
        return f'{status.players.online} players online'
    except Exception:
        return "Server Offline"

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    update_status.start()

@tasks.loop(minutes=5)  # Update every 5 minutes
async def update_status():
    status = get_server_status()
    await client.change_presence(activity=discord.Game(name=status))

client.run(TOKEN)
