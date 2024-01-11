class InteractiveObject:
    """进行交互的对象"""
    pass


class InteractiveObjectImplA:
    """实现类A"""
    pass


class InteractiveObjectImplB:
    """实现类B"""
    pass


class Meditor:
    """中介类"""

    def __init__(self):
        self.__interactiveObjA = InteractiveObjectImplA()
        self.__interactiveObjB = InteractiveObjectImplB()

    def interactive(self):
        """进行交互的操作"""
        pass

