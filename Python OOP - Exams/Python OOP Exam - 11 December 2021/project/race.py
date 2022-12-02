from project.validation.validation import Validation


class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.driver_name_validation(value)
        self.__name = value
