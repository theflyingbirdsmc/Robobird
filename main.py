import discord
import json
from discord.ext import commands, tasks
from mcstatus import JavaServer

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

TOKEN = "$Secrets.TOKEN"
IP_ADDRESS = "mc.theflyingbirds.net"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Update the Minecraft server status
async def update_status():
    server = JavaServer.lookup(IP_ADDRESS)
    try:
        status = server.status()
        channel_name = f"🟢 Online: {status.players.online}/{status.players.max}"
    except Exception as e:
        print(f"Error fetching server status: {e}")
        channel_name = "🔴 Offline"

    return channel_name

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    
    guild = bot.guilds[0]  # Assuming the bot is in only one server
    if config["channel_id"]:
        channel = guild.get_channel(config["channel_id"])
    else:
        # Create new voice channel at the top of the server
        overwrites = {guild.default_role: discord.PermissionOverwrite(connect=False)}
        channel = await guild.create_voice_channel("minecraft-server-status", position=0, overwrites=overwrites)
        # Save channel ID in the config file
        config["channel_id"] = channel.id
        with open("config.json", "w") as config_file:
            json.dump(config, config_file)
    
    update_status_loop.start(channel)

@tasks.loop(minutes=5)
async def update_status_loop(channel):
    new_name = await update_status()
    await channel.edit(name=new_name)

bot.run(TOKEN)
