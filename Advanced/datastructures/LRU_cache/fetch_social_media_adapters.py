from abc import ABC, abstractmethod
import requests

class SocialMediaAdapter(ABC):
    @abstractmethod
    def post_message(self, message: str) -> dict:
        """ Post a message to social media"""
        pass

    @abstractmethod
    def fetch_posts(self, user_id: str) -> list:
        """ Fetch recent messages of a user"""
        pass


# for example: Twitter (X)
class TwitterAdapter(SocialMediaAdapter):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.twitter.com/2/"

    def post_message(self, message: str):
        url = f'{self.base_url}tweets'
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"text": message}
        response = requests.post(url, json=data, headers=headers)
        return response.json()
    
    def fetch_posts(self, user_id: str) -> list:
        url = f"{self.base_url}users/{user_id}/tweets"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        return response.json().get("data", [])
    
    
# instead of calling adapters separately, we use our manager
# to interact with adapters (this way, we can have multiple adapters)
class SocialMediaManager:
    def __init__(self):
        self.adapters = {}

    def register_adapter(self, platform: str, adapter: SocialMediaAdapter):
        self.adapters[platform] = adapter

    def post_message(self, platform: str, message: str):
        if platform in self.adapters:
            return self.adapters[platform].post_message(message)
        raise ValueError(f"No adapter found for platform {platform}")

    def fetch_posts(self, platform: str, user_id: str):
        if platform in self.adapters:
            return self.adapters[platform].fetch_posts(user_id)
        raise ValueError(f"No adapter found for platform {platform}")