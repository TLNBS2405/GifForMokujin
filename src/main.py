from src import ImgurClient
import json
import tkinter as tk
from tkinter import filedialog

with open("config.json") as config_json:
    config_data = json.load(config_json)

ic = ImgurClient.ImgurClient(config_data["client_ID"], config_data["access_token"])
tk.Tk().withdraw()
dirname = filedialog.askdirectory(initialdir="/", title='Please select a directory', mustexist=True)

if dirname:
    error = ic.upload_folder(dirname)
    if error:
        print("Error:", error)
print("finished")
