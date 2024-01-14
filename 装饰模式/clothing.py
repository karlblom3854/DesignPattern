from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print("着装：")


class Engineer(Person):
    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def wear(self):
        print(f"我是{self.get_skill()}工程师{self._name}", end="，")
        super().wear()


class Teacher(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    def get_title(self):
        return self.__title

    def wear(self):
        print(f"我是{self.get_title()}{self._name}", end="，")
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


class CausalPantDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("\t休闲裤")


class BeltDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("\t腰带")


class LeatherShoeDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("\t皮鞋")


class KnittedSweeterDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("\t针织毛衣")


class WhiteShirtDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("\t白色衬衫")


class GlassDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("\t眼镜")


if __name__ == '__main__':
    tony = Engineer("Tony", "前端")
    pant = CausalPantDecorator(tony)
    belt = BeltDecorator(pant)
    shoes = LeatherShoeDecorator(belt)
    shirt = WhiteShirtDecorator(shoes)
    sweater = KnittedSweeterDecorator(shirt)
    glasses = GlassDecorator(sweater)
    glasses.wear()

    carl = GlassDecorator(CausalPantDecorator(WhiteShirtDecorator(LeatherShoeDecorator(
        Teacher("Carl", "教授")))))
    carl.wear()

