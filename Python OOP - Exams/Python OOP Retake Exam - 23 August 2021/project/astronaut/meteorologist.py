from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    BREATH_COST = 15

    def __init__(self, name: str):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= self.BREATH_COST

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

