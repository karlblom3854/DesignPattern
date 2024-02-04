from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def request(self, content):
        pass


class ReadSubject(Subject):
    def request(self, content):
        print(f"ReadSubject do something...")


class ProxySubject(Subject):
    def __init__(self, name, subject):
        super().__init__(name)
        self._subject = subject

    def request(self, content):
        self.pre_process()
        if self._subject is not None:
            self._subject.request(content)

        self.post_process()

    @abstractmethod
    def pre_process(self):
        pass

    @abstractmethod
    def post_process(self):
        pass

