from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Drawing Circle...")


class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle...")


class ShapeDecorator(Shape):
    def __init__(self, shape):
        self._shape = shape

    @abstractmethod
    def decorate(self):
        pass

    def draw(self):
        self._shape.draw()
        self.decorate()


class RedShapeDecorator(ShapeDecorator):
    def __init__(self, shape):
        super().__init__(shape)

    def decorate(self):
        print("\tBorder Color: Red")


if __name__ == '__main__':
    circle = Circle()
    rectangle = Rectangle()

    red_circle = RedShapeDecorator(circle)
    red_rectangle = RedShapeDecorator(rectangle)

    red_circle.draw()
    red_rectangle.draw()
