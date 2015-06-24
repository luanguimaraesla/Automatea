__author__ = 'luan'

class TeaTaste:
    def __init__(self, name, manufacturer = None, origin = None, expiration_date = None, description = None, photo_path = None):
        self.name = name
        self.manufacturer = manufacturer
        self.origin = origin
        self.expiration_date = expiration_date
        self.description = description
        self.photo_path = photo_path

    def change_photo_path(self, new_photo_path):
        if isinstance(new_photo_path, str):
            self.photo_path = new_photo_path
        else:
            raise IOError