__author__ = 'luan'

from models import TeaTasteDB, Manufacturer

class TeaTaste:
    def __init__(self, name, manufacturer = None, origin = None, expiration_date = None, description = None, photo_path = None):
        self.on_DB = Manufacturer(name = name, origin = origin, expiration_date = expiration_date,
                                  description = description, photo_path = photo_path)
        self.name = name
        self.set_manufacturer(manufacturer, self.on_DB)
        self.origin = origin
        self.expiration_date = expiration_date
        self.description = description
        self.photo_path = photo_path

    def set_manufacturer(self, manufacturer, on_DB):
        manufacturer_list = Manufacturer.objects.all()
        for each_manufacturer in manufacturer_list:
            if each_manufacturer.name == manufacturer:
                on_DB.manufacturer_set.add(each_manufacturer)
                break
        else:
            on_DB.manufacturer_set.create(name = manufacturer)

    def change_photo_path(self, new_photo_path):
        if isinstance(new_photo_path, str):
            self.photo_path = new_photo_path
        else:
            raise IOError