from abc import ABC, abstractmethod


class Karoseria(ABC):
    __elementy = {}

    def __init__(self, parametry: set = []):
        nazwa_klasy = self.__class__.__name__
        if list is not []:
            if nazwa_klasy not in self.__elementy:
                self.__elementy.update({nazwa_klasy: {}})
            self.__elementy[nazwa_klasy].update(parametry)

    def get_elementy(self):
        return self.__elementy

    @abstractmethod
    def dodaj_element(self):
        pass

    @abstractmethod
    def usun_element(self):
        pass

    @abstractmethod
    def testuj(self):
        pass