from imgur_python import Imgur
import glob, time
import ctypes

class ImgurClient:

    def __init__(self, client_id, access_token):
        self.ic = Imgur({'client_id': client_id, 'access_token': access_token})

    def create_album(self, name: str):
        print("creating album: ", name)
        album = self.ic.album_create([], name, '', 'public')
        album_id = album['response']['data']['id']
        return album_id

    def upload_gif(self, path: str, title: str = None, desc: str = None, album_hash: str = None):
        print("uploading ",path)
        response = self.ic.image_upload(filename=path, title=title, description=desc, album=album_hash)
        return response

    def upload_folder(self, path: str):
        error_status = {}
        album_name = path.split("\\")[-1]
        album_id = self.create_album(album_name)

        all_files = glob.glob(path + "\\*")
        for file in all_files:
            file_name = file.split("\\")[-1]
            status = self.upload_gif(path=file, title=file_name, album_hash=album_id)
            if status["status"] != 200:
                msg = {"status": status, "file": file_name, "next": "retry upload in an hour" }
                ctypes.windll.user32.MessageBoxW(0, msg, "Error", 1)
                time.sleep(3600)

                status = self.upload_gif(path=file, title=file_name, album_hash=album_id)
                if status["status"] == 200:
                    msg = f'File {file_name} upload successfully continued'
                    ctypes.windll.user32.MessageBoxW(0, msg, "OK", 1)
                    error_status[file] = status


        return error_status
