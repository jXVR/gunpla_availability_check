import os
import requests
import time
from datetime import datetime
from discordwebhook import Discord

discord_webhook = os.environ["WEBHOOK_URL"]
discord = Discord(url=discord_webhook)

aerial_urls = {
    "Kanton": "https://katonsklep.pl/hg/3310-hg-1144-gundam-aerial.html",
    "Zinc Mecha": "https://www.zincmecha.com/product/hgtwfm-1-144-gundam-aerial/",
    "To Ja Lece": "https://www.tojalece.pl/hg-1-144-gundam-aerial",
    "Plastiq": "https://plastiq.pl/hg-1-144-gundam-aerial,id3009.html"
}

lfrith_urls = {
    "Kanton": "https://katonsklep.pl/hg/3311-hg-1144-gundam-lfrith.html",
    "Zinc Mecha": "https://www.zincmecha.com/product/hgtwfm-1-144-gundam-lfrith/",
    "To Ja Lece": "https://www.tojalece.pl/hg-1-144-gundam-aerial https://www.tojalece.pl/hg-1-144-gundam-lfrith",
    "Plastiq": "https://plastiq.pl/hg-1-144-gundam-lfrith,id3010.html"
}

keywords = {
    "Kanton": "Dostępny",
    "Zinc Mecha": "Dodaj do koszyka",
    "To Ja Lece": "Dostępny",
    "Plastiq": "Dodaj do koszyka"
}

message = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for key, item in keywords.items():
    message += f"\n\nChecking {key} shop:"

    page = requests.get(aerial_urls[key])
    if page.text.find(item)>0:
      message += f"\nAerial available in {key} shop"
      message += "\nLink " + aerial_urls[key]
    else:
      message += '\nAerial - Out of stock'

    page = requests.get(lfrith_urls[key])
    if page.text.find(item)>0:
      message += f"\nLfrith available in {key} shop"
      message += "\nLink " + lfrith_urls[key]
    else:
      message += '\nLfrith - Out of stock'

discord.post(
    content=message,
    username="Miorine Rembran",
    avatar_url="https://static.wikia.nocookie.net/universal-warriors/images/c/ce/Miorinep.jpg/revision/latest?cb=20221112125952"
)
