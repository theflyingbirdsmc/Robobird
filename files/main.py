import os
import discord
import requests
from discord.ext import tasks

TOKEN = os.environ['BOT_TOKEN']
IP_ADDRESS = os.environ['IP']

# Set up the necessary intents
intents = discord.Intents.default()

client = discord.Client(intents=intents)

def get_server_status(ip_address):
    url = f"https://api.mcstatus.io/v2/status/java/{ip_address}"
    try:
        response = requests.get(url)
        data = response.json()
        if data["online"]:
            players_online = data["players"]["online"]
            return f'{players_online} players online'
        else:
            return "Server Offline"
    except Exception as e:
        print(f"Error: {e}")
        return "Error checking server status"

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    update_status.start()

@tasks.loop(minutes=5)  # Update every 5 minutes
async def update_status():
    status = get_server_status(IP_ADDRESS)
    await client.change_presence(activity=discord.Game(name=status))

client.run(TOKEN)
