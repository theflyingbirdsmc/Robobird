import os
import discord
import mcstatus
from discord.ext import tasks

TOKEN = os.environ['BOT_TOKEN']
IP_ADDRESS = os.environ['IP']

client = discord.Client()

def get_server_status():
    try:
        server = mcstatus.lookup(IP_ADDRESS)
        status = server.status()
        return f'{status.players.online} players online'
    except Exception as e:
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
