import json
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import os

# Configuration
server = str(os.getenv("SERVER"))
webhook_url = str(os.getenv("WEBHOOK_URL"))

# api
api_url = f"https://api.mcsrvstat.us/3/{server}"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()

    online = data.get("players").get("online")
    players = data.get("players").get("list")
    version = data.get("version")
    software = data.get("software")
    ip = data.get("ip")
    hostname = data.get("hostname")
    port = data.get("port")
    motd = data.get("motd").get("clean")
    motd = motd[0]

    players_online = ""

    try:
        for i in players:
            players_online += "\n`" + i["name"] + "`"
    except: TypeError

webhook = DiscordWebhook(url=webhook_url)

embed = DiscordEmbed(title="__Server Query__", description=f"`{hostname}:{port}` \n> {motd}", color="03b2f8")
embed.add_embed_field(name=f"__Players Online:__ {online}", value=f"{players_online}")
embed.set_footer(text=f"{ip} {software} {version}", icon_url="https://cdn.icon-icons.com/icons2/2699/PNG/512/minecraft_logo_icon_168974.png")
embed.set_timestamp()
embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/2072/PNG/512/data_hosting_information_internet_security_server_storage_icon_127051.png")

webhook.add_embed(embed)
webhook.execute()


