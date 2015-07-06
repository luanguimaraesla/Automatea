__author__ = 'luan'

class Person:
    def __init__(self, name, mail, photo_path = None):
        self.name = name
        self.mail = mail
        self.photo_path = photo_path

    def change_photo_path(self, new_photo_path):
        if isinstance(new_photo_path, str):
            self.photo_path = new_photo_path
        else:
            raise IOError