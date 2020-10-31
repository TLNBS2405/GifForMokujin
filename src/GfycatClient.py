
import requests


class GfycatClient:

    def __init__(self, client_id, client_secret):
        json_data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        }

        response = requests.post('https://api.gfycat.com/v1/oauth/token', json=json_data)
        if response.status_code == 200:
            self.access_token = response.json()["access_token"]
            print("access_token created")

    def upload_gif(self, path: str, title: str = None):
        print("uploading ", path)
        return ""

    def create_album(self, name: str):
        URL = "https://api.gfycat.com/v1/me/bookmark-folders"
        json_data = {
            "folderName": name
        }
        header = {'authorization': f'Bearer {self.access_token}'}
        response = requests.get(URL, headers=header)
        print(response)
        if response.status_code == 200:
            print(f'album {name} created')
