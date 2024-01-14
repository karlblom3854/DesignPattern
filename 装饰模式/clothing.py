from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def wear(self):
        print("着装")


class Engineer(Person):
    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    def wear(self):
        print(f"我是{self.__skill}工程师{self.__name}", end="，")
        super().wear()

class Teacher(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    def wear(self):
        print(f"我是{self.__title}{self.__name}", end="，")
        super().wear()


class ClothingDecorator(Person):
    def __init__(self, person):
        self._decorated = person

    def wear(self):
        self._decorated.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass

