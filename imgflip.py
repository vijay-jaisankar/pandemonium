import requests
import random
from typing import Optional

"""
    @method get_meme_url
        Calls the ImgFlip API to get a random meme URL
    @ref https://imgflip.com/api
"""
def get_meme_url() -> Optional[str]:
    try:
        # Make the request to imgflip API
        r = requests.get("https://api.imgflip.com/get_memes")
        if r.status_code != 200:
            return None
        
        # Get details of a random meme
        meme_details = r.json()["data"]["memes"]
        meme_object = random.choice(meme_details)
        return str(meme_object["url"])
    
    except Exception as e:
        print(f"Error occured: {e}")
        return None