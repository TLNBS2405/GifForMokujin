import abc


class UploaderInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'createAlbum') and
                callable(subclass.createAlbum) and
                hasattr(subclass, 'uploadGif') and
                callable(subclass.uploadGif)and
                hasattr(subclass, 'uploadFolder') and
                callable(subclass.uploadFolder))

    @abc.abstractmethod
    def createAlbum(self, name:str):
        pass

    @abc.abstractmethod
    def uploadGif(self, path: str):
        pass

    @abc.abstractmethod
    def uploadFolder(self, path: str):
        pass
