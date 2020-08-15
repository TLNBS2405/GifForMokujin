from src import ImgurClient
import json
from tkfilebrowser import askopendirnames
import tkinter as tk
from tkinter import ttk


with open("config.json") as config_json:
    config_data = json.load(config_json)

dirname=""

ic = ImgurClient.ImgurClient(config_data["client_ID"], config_data["access_token"])
root = tk.Tk()
style = ttk.Style(root)
style.theme_use("alt")
root.configure(bg=style.lookup('TFrame', 'background'))

def c_open_dir():
    dirnames = askopendirnames(parent=root, initialdir='/', initialfile='tmp')
    if dirnames:
        for dir_name in dirnames:
            error = ic.upload_folder(dir_name)
            if error:
                print("Error:", error)
    print("finished")

ttk.Button(root, text="Open folder", command=c_open_dir).grid(row=2, column=1, padx=4, pady=4, sticky='ew')
root.mainloop()

