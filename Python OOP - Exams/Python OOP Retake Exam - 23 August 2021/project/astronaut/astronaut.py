from project.validator import Validation
from abc import ABC, abstractmethod


class Astronaut(ABC):
    BREATH_COST = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.astronaut_name(value)
        self.__name = value

    @abstractmethod
    def breathe(self):
        pass

    def increase_oxygen(self, amount: int):
        pass
