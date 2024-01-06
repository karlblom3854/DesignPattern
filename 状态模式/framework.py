from abc import ABCMeta, abstractmethod


class Context(metaclass=ABCMeta):
    def __init__(self):
        self.__states = []
        self.__current_state = None
        self.__state_info = 0  # 当某个状态是由多个变量确定时可以将其单独定义为一个类

    def add_state(self, state):
        if state not in self.__states:
            self.__states.append(state)

    def get_state(self):
        return self.__current_state

    def change_state(self, state):
        if state is None:
            return False
        if self.__current_state is None:
            print(f"初始状态：{state.get_name()}")
        elif self.__current_state == state:
            print(f"维持原始状态：{state.get_name()}")
        else:
            print(f"由{self.__current_state.get_name()}状态变为{state.get_name()}")
        self.__current_state = state
        self.add_state(state)  # 添加状态
        return True
        # if self.__current_state is not state:

    def _set_state_info(self, state_info):
        self.__state_info = state_info
        for state in self.__states:
            if state.is_match(state_info):
                self.change_state(state)

    def get_state_info(self):
        return self.__state_info


class State:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def is_match(self, state_info):
        """状态的属性stateInfo是否在当前的状态范围内"""
        pass

    @abstractmethod
    def behavior(self, context):
        pass
