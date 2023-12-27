from framework import Observer, Observable


class WaterHeater(Observable):
    """定义被观察对象：热水器，继承父类被观察者"""
    def __init__(self, temperature):
        super().__init__()  # 作用：初始化被观察者列表
        self.__temperature = temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        self.notify_observers()

    def get_temperature(self):
        return self.__temperature


class WashingMode(Observer):
    def update(self, water_heater):
        current_temperature = water_heater.get_temperature()
        if 50 <= current_temperature < 70:
            print(f"此时水温为{current_temperature}，可洗澡！")


class DrinkingMode(Observer):
    def update(self, water_heater):
        current_temperature = water_heater.get_temperature()
        if current_temperature >= 100:
            print(f"此时水温为{current_temperature}，可饮用！")


if __name__ == '__main__':
    my_water_heater = WaterHeater(15)
    wash_mode = WashingMode()
    drink_mode = DrinkingMode()

    my_water_heater.add_observer(wash_mode)
    my_water_heater.add_observer(drink_mode)

    my_water_heater.set_temperature(20)
    my_water_heater.set_temperature(60)
    my_water_heater.set_temperature(100)



