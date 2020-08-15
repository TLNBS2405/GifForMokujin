from src import ImgurClient
import json

with open("config.json") as config_json:
    config_data = json.load(config_json)

ic = ImgurClient.ImgurClient(config_data["client_ID"], config_data["access_token"])

response = ic.uploadGif("test/test.png")

print(response)
