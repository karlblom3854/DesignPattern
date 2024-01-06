from framework import Context, State


class Water(Context):
    def __init__(self):
        super().__init__()
        self.add_state(SolidState("固态"))
        self.add_state(LiquidState("液态"))
        self.add_state(GaseousState("气态"))
        self.set_temperature(25.0)

    def get_temperature(self):
        return self.get_state_info()

    def set_temperature(self, temperature):
        self._set_state_info(temperature)

    def rise_temperature(self, step):
        self.set_temperature(self.get_temperature() + step)

    def reduce_temperature(self, step):
        self.set_temperature(self.get_temperature() - step)

    def behavior(self):
        state = self.get_state()
        if isinstance(state, State):
            state.behavior(self)


# 单例的修饰器
def singleton(cls, *args, **kwargs):
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton


@singleton
class SolidState(State):
    """固态"""
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info < 0

    def behavior(self, context):
        print(f"\t固态，当前温度：{context.get_state_info()}\n")


@singleton
class LiquidState(State):
    """液态"""
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return 0 <= state_info < 100

    def behavior(self, context):
        print(f"\t液态，当前温度：{context.get_state_info()}\n")


@singleton
class GaseousState(State):
    """气态"""
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info >= 100

    def behavior(self, context):
        print(f"\t气态，当前温度：{context.get_state_info()}\n")


if __name__ == '__main__':

    water = Water()
    water.behavior()

    water.set_temperature(-10)
    water.behavior()

    water.reduce_temperature(1)
    water.behavior()

    water.rise_temperature(50)
    water.behavior()

    water.rise_temperature(65)
    water.behavior()
