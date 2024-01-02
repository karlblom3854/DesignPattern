from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """定义观察者父类"""
    @abstractmethod
    def update(self, observable, info):
        """观察者用于更新状态的抽象方法"""
        pass


class Observable:
    """定义被观察者父类"""

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        """"添加观察者"""
        self.__observers.append(observer)

    def remove_observer(self, observer):
        """移除观察者"""
        self.__observers.remove(observer)

    def notify_observers(self, info=None):
        """将自身信息变化通知给所有观察者"""
        for o in self.__observers:
            o.update(self, info)
