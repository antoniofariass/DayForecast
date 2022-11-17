from random import randint


class GenerateID:
    def __init__(self,username) -> None:
        self._username = username
        self._id = randint(00000,99999)
        self._city = ''

    @property
    def username(self):
        return self._username
    
    @property
    def id(self):
        return self._id
    
    @property
    def city(self):
        return self._city

    def associate_city(self,city):
        self._city = city


