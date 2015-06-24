__author__ = 'luan'

from .person import Person

class User(Person):
    def __init__(self, nick_name, password, name, mail, photo_path = None):
        Person.__init__(self, name, mail, photo_path)

        self.nick_name = nick_name
        #Lembrar de salgar a senha com Hash
        self.password = password
        self.preferred_tea_list = []

    #def add_a_preferred_tea(self, ):