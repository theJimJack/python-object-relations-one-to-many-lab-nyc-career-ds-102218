# import car class here
from car import Car

class Owner:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def find_my_cars(self):
        object_list = list(filter(lambda x:x.owner==self.name,Car._all))
        FMC = []
        for i in object_list:
            FMC.append(str(i.make)+' '+str(i.model))
        return FMC
