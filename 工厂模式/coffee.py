from abc import ABCMeta, abstractmethod


class Coffee(metaclass=ABCMeta):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def get_taste(self):
        pass

