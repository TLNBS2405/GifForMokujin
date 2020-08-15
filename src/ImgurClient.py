from imgur_python import Imgur
import glob

class ImgurClient:

    def __init__(self, client_id, access_token):
        self.ic = Imgur({'client_id': client_id, 'access_token': access_token})

    def create_album(self, name: str):

        album =  self.ic.album_create([], name, '', 'public')
        print(album)
        album_id = album['response']['data']['id']
        return album_id

    def upload_gif(self, path: str, title: str = None, desc : str = None, album_hash: str = None):

        response = self.ic.image_upload(path, title, desc, album=album_hash)
        return response

    def upload_folder(self, path: str):
        all_status = []
        last_part = path.split("/")[-1]

        album_id = self.create_album(last_part)

        all_files = glob.glob(path+"\\*")
        for file in all_files:
            status = self.upload_gif(file,album_hash=album_id)["status"]
            all_status.append(status)
        return all_status

