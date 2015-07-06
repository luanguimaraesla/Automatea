from django.db import models


# Create your models here.
_HIGH_SUGAR = 25 #g
_MID_SUGAR = 15  #g
_LOW_SUGAR = 7   #g
_NO_SUGAR = 0

_HIGH_WATER = 500 #ml
_MID_WATER = 250  #ml
_LOW_WATER = 100  #ml


class Manufacturerdb(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Teatastedb(models.Model):
    name = models.CharField(max_length = 30)
    manufacturer = models.ForeignKey(Manufacturerdb, null=True, blank=True)
    origin = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500)
    photo_path = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

    def set_manufacturer(self, manufacturer):
        manufacturer_list = Manufacturerdb.objects.all()
        for each_manufacturer in manufacturer_list:
            if each_manufacturer.name == manufacturer:
                each_manufacturer.teatastedb_set.add(self)
                break
        else:
            newMf = Manufacturerdb(name = manufacturer)
            newMf.save()
            newMf.teatastedb_set.add(self)
            newMf.save()

class Teadb(models.Model):
    name = models.CharField(max_length = 30)
    water_ml = models.IntegerField(default = _MID_WATER)
    sugar_wg = models.IntegerField(default = _NO_SUGAR)
    taste_list = models.ManyToManyField(Teatastedb, null=True, blank=True)

    def __str__(self):
        return self.name

class Userdb(models.Model):
    name = models.CharField(max_length = 50)
    mail = models.CharField(max_length = 30)
    photo_path = models.CharField(max_length = 50)
    nick_name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    my_tea_list = models.ManyToManyField(Teadb, null=True, blank=True)

    def __str__(self):
        return self.name

    def add_a_tea(self, tea):
        if not isinstance(tea, Teadb):
            raise IOError

        self.my_tea_list.add(tea)

    def create_tea(self, name, taste, water = 250, sugar = 0):
        newtea = self.my_tea_list.create(name = name, water_ml = water, sugar_wg = sugar)
        if taste:
            if isinstance(taste, Teatastedb):
                self.my_tea_list.taste_list.add(taste)
            elif isinstance(taste, list):
                for each_taste in taste:
                    self.my_tea_list.taste_list.add(taste)

        newtea.save()
        return newtea

    def add_new_taste(self, name, manufacturer = None,
                      origin = None,
                      description = None, photo_path = None):

        self.save()
        tea = self.create_tea(name = name, taste = None)
        teataste = tea.taste_list.create(name = name, origin = origin, description = description, photo_path = photo_path)
        teataste.set_manufacturer(manufacturer)
        teataste.save()

    def change_photo_path(self, new_photo_path):
        if isinstance(new_photo_path, str):
            self.photo_path = new_photo_path
        else:
            raise IOError

        self.save()

    def get_user_by_id(self, user_id):
        return Userdb.objects.get(pk = id)

    def get_id_by_name(self, user_name):
        return Userdb.objects.get(name = user_name)

    def get_all_users(self):
        return Userdb.objects.all()

