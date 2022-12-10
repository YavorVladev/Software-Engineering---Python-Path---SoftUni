from abc import ABC, abstractmethod
from project.validation.validation import Validation


class Delicacy(ABC):
    def __init__(self, name: str, portion: int, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.delicacy_name_validator(value)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validation.delicacy_price_validator(value)
        self.__price = value

    @abstractmethod
    def details(self):
        ...
