# Minecraft Server Status Discord Bot Documentation
This Python script creates a Discord bot that automatically updates a voice channel name with the status of a specified Minecraft server using the mcstatus library. The bot uses the discord.py library for connecting to Discord and managing the voice channel.

## Required Libraries
`discord.py`: Discord API Wrapper for Python

`mcstatus`: Library for checking the status of Minecraft servers

## Configuration
`config.json` is used to store the channel ID of the voice channel where the status is displayed. The file has the following structure:

```json
Copy code
{
    "channel_id": null
}
```

`TOKEN` (line 10): Replace the empty string with your Discord bot token.

`IP_ADDRESS` (line 11): Replace the IP address with the desired Minecraft server's IP address.

## Functions
### update_status()
This function fetches the status of the Minecraft server and returns a formatted channel name including the server's online or offline status and player count.

### on_ready()
This event is triggered when the bot is connected and ready. It creates a new voice channel at the top of the server if the channel ID isn't found in the `config.json` file, saves the channel ID, and starts the `update_status_loop` task.

### update_status_loop
This task runs every 5 minutes and updates the channel name with the Minecraft server's status.

### Setup and Running the Bot
Install required libraries:

```
pip install discord.py mcstatus
```
Replace the `TOKEN` variable with your Discord bot token and set the desired Minecraft server IP address.

Run the script:

```
python your_script_name.py
```
### Customization
You can adjust the update interval by changing the `minutes` parameter in the `tasks.loop` decorator (line 44). For example, `minutes=10` will update the channel name every 10 minutes.
