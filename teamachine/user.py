__author__ = 'luan'

from person import Person
from tea import Tea
from teataste import TeaTaste
from models import Userdb

class User(Person):
    def __init__(self, nick_name, password, name, mail, photo_path = None):
        Person.__init__(self, name, mail, photo_path)

        self.nick_name = nick_name
        self.password = password
        self.my_tea_list = []

    def add_a_preferred_tea(self, tea):
        if not isinstance(tea, Tea):
            raise IOError
        self.my_tea_list.append(tea)

    def create_tea(self, name, taste, water_ml = Tea._MID_WATER, sugar_wg = Tea._NO_SUGAR):
        new_tea = Tea(name, taste, water_ml, sugar_wg)
        self.add_a_preferred_tea(new_tea)
        return new_tea

    def add_new_taste(self, name, manufacturer = None,
                      origin = None, expiration_date = None,
                      description = None, photo_path = None):

        new_taste = TeaTaste(name, manufacturer, origin, expiration_date, description, photo_path)
        self.create_tea(name, new_taste)

        return new_taste



    #def order(self, Tea):