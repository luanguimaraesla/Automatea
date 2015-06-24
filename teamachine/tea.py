__author__ = 'luan'

from teataste import TeaTaste

class Tea:
    _HIGH_SUGAR = 25 #g
    _MID_SUGAR = 15  #g
    _LOW_SUGAR = 7   #g
    _NO_SUGAR = 0

    _HIGH_WATER = 500 #ml
    _MID_WATER = 250  #ml
    _LOW_WATER = 100  #ml

    def __init__(self, name, taste, water_ml = _MID_WATER, sugar_wg = _MID_SUGAR):
        self.name = name
        self.taste_list = []
        self.append_taste_list(taste)
        self.water_ml = water_ml
        self.sugar_wg = sugar_wg

    def append_taste_list(self, taste):
        if not taste:
            raise IOError
        elif isinstance(taste, TeaTaste):
            self.taste_list.append(taste)
        elif isinstance(taste, list) or isinstance(taste, tuple):
            self.taste_list.extend(list(taste))