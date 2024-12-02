import requests
import random
from typing import Optional

def get_meme_url() -> Optional[str]:
    try:
        response = requests.get("https://api.imgflip.com/get_memes")
        response.raise_for_status()  # Ensure request is successful

        # Safely access API data
        data = response.json()
        if "data" in data and "memes" in data["data"]:
            meme_details = data["data"]["memes"]
            meme_object = random.choice(meme_details)
            return str(meme_object["url"])
        else:
            print("Unexpected API response format.")
            return None

    except Exception as e:
        print(f"Error occurred: {e}")
        return None
