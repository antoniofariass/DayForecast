from random import randint


class GenerateID:
    def __init__(self,username:str) -> None:
        self.username = username
        self.__id = randint(00000,99999)
        self._city = ''

    @property
    def username(self):
        return self.username
    
    @property
    def id(self):
        return self.__id
    
    @username.setter
    def username(self,new_username):
        self.username = new_username
    
    @id.setter
    def id(self,new_id):
        self.__id = new_id
        
    def associate_city(self,city):
        self._city = city


