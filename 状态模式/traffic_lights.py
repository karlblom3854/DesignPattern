from framework import Context, State

# 假设你正在开发一个交通信号灯控制系统。
# 请设计一个使用状态模式的交通信号灯系统，其中包括红灯、黄灯和绿灯三种状态，并能够实现状态之间的切换。
# 以下是问题的一些建议要点：
# 定义状态接口： 创建一个State接口，其中包含表示不同状态的方法，例如turn_on。
# 实现具体状态类： 创建三个具体状态类，分别表示红灯、黄灯和绿灯。每个状态类都实现State接口中的方法。
# 定义上下文类： 创建一个上下文类，例如TrafficLight，该类包含一个当前状态属性，以及用于切换状态的方法，例如change_state。
# 测试： 编写一个测试脚本，创建交通信号灯对象，并模拟交通信号灯的状态变化，演示状态之间的切换。


class TrafficLight(Context):
    def __init__(self):
        super().__init__()
        self.add_state(RedLight("红灯"))
        self.add_state(GreenLight("绿灯"))
        self.add_state(YellowLight("黄灯"))
        self.turn_on("Green")

    def turn_on(self, light_color):
        self._set_state_info(light_color)

    def get_light_color(self):
        return self.get_state_info()

    def behavior(self):
        state = self.get_state()
        if isinstance(state, State):
            state.behavior(self)


def singleton(cls, *args, **kwargs):
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton


@singleton
class GreenLight(State):
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info.lower() == "green"

    def behavior(self, context):
        print(f"\t此时交通信号灯为{context.get_state_info().title()}\t\t🟢🟢🟢\t\t🉑以通行！\n")


@singleton
class YellowLight(State):
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info.lower() == "yellow"

    def behavior(self, context):
        print(f"\t此时交通信号灯为{context.get_state_info().title()}\t\t🟡🟡🟡\t\t⌛️请等待！\n")


@singleton
class RedLight(State):
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info.lower() == "red"

    def behavior(self, context):
        print(f"\t此时交通信号灯为{context.get_state_info().title()}\t\t🔴🔴🔴\t\t🈲止通行！\n")


if __name__ == '__main__':
    traffic_light = TrafficLight()
    traffic_light.behavior()

    traffic_light.turn_on("yellow")
    traffic_light.behavior()

    traffic_light.turn_on("red")
    traffic_light.behavior()

    traffic_light.turn_on("green")
    traffic_light.behavior()
