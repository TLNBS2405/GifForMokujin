from imgur_python import Imgur



class ImgurClient:

    def __init__(self, client_id, access_token):
        self.client_id = client_id
        self.access_token = access_token

    def createAlbum(self, name: str):
        print("")

    def uploadGif(self, path: str, album_hash: str = None):

        ic = Imgur({'client_id': self.client_id, 'access_token': self.access_token})
        response = ic.image_upload(path, 'Untitled', 'My first image upload', album=album_hash)
        return response

    def uploadFolder(self, path: str):
        print("")
