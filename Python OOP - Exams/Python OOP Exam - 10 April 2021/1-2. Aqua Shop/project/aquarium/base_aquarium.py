from abc import ABC, abstractmethod
from project.validation.validation import Validation


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.valid_aquarium_name(value, "Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish: object):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        fish_type = fish.__class__.__name__

        if fish_type in ("FreshwaterFish", "SaltwaterFish"):
            self.fish.append(fish)
            return f"Successfully added {fish_type} to {self.name}."

    def remove_fish(self, fish: object):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: object):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = [f"{self.name}:", f"Fish: "]
        if self.fish:
            result[1] += " ".join(f.name for f in self.fish)
        else:
            result[1] += "none"

        result.append(f"Decorations: {len(self.decorations)}\n"
                      f"Comfort: {self.calculate_comfort()}")

        return '\n'.join(result)
