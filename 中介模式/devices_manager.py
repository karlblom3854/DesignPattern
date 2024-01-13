from abc import ABCMeta, abstractmethod
from enum import Enum


class DeviceType(Enum):
    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3


class DeviceItem:
    def __init__(self, device_id, name, device_type, is_default):
        self.__id = device_id
        self.__name = name
        self.__device_type = device_type
        self.__is_default = is_default

    def __str__(self):
        return (f"设备ID：{str(self.__id)}，设备名称：{str(self.__name)}，"
                f"设备类型{str(self.__device_type)}， 是否默认设备：{str(self.__is_default)}")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__device_type

    def is_default(self):
        return self.__is_default


class DeviceList:
    def __init__(self):
        self.__device_list = []

    def add_device(self, device_item):
        self.__device_list.append(device_item)

    def get_count(self):
        return len(self.__device_list)

    def get_by_idx(self, idx):
        if idx < 0 or idx >= len(self.__device_list):
            return None
        else:
            return self.__device_list[idx]

    def get_by_id(self, device_id):
        for device_item in self.__device_list:
            if device_item.get_id() == device_id:
                return device_item


class DeviceManager(metaclass=ABCMeta):
    def __init__(self):
        self.__cur_device_id = None

    @abstractmethod
    def enumerate_devices(self):
        pass

    @abstractmethod
    def get_cur_device_id(self):
        pass

    @abstractmethod
    def activate(self, device_id):
        pass


class CameraManager(DeviceManager):
    def __init__(self):
        super().__init__()

    def enumerate_devices(self):
        """枚举设备列表"""
        devices = DeviceList()
        devices.add_device(DeviceItem("369dd760-893b-4fe0-89b1-671eca0f022", "Camera 1",
                                      DeviceType.TypeCamera, True))
        devices.add_device(DeviceItem("369dd760-893b-4fe0-89b1-897sars898", "Camera 2",
                                      DeviceType.TypeCamera, False))
        return devices

    def get_cur_device_id(self):
        return self.__cur_device_id

    def activate(self, device_id):
        self.__cur_device_id = device_id


class DeviceUtil:
    def __init__(self):
        self.__managers = {}
        self.__managers[DeviceType.TypeCamera] = CameraManager()
        # 暂不添加其他设备

    def __get_device_manager(self, device_type):
        return self.__managers[device_type]

    def get_device_list(self, device_type):
        return self.__get_device_manager(device_type).enumerate_devices()

    def activate(self, device_type, device_id):
        self.__get_device_manager(device_type).activate(device_id)

    def get_cur_device_id(self, device_type):
        return self.__get_device_manager(device_type).get_cur_device_id()


if __name__ == '__main__':
    device_util = DeviceUtil()
    device_list = device_util.get_device_list(DeviceType.TypeCamera)
    print(f"相机设备列表：")
    if device_list.get_count() > 0:
        device_util.activate(DeviceType.TypeCamera, device_list.get_by_idx(0).get_id())
    for idx in range(device_list.get_count()):
        device = device_list.get_by_idx(idx)
        print(device)
    print(f"当前使用的设备： {device_list.get_by_id(device_util.get_cur_device_id(DeviceType.TypeCamera)).get_name()}")
