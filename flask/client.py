import requests
from dotenv import load_dotenv
import os

def hypixelBazaarClient():
    load_dotenv()
    response = requests.get("https://api.hypixel.net/skyblock/bazaar?key={}".format(os.getenv("API_KEY")))

    if (response.status_code != 200):
        raise Exception("API error")

    response = response.json()

    return(response)