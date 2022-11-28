from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    BREATH_COST = 10

    def __init__(self, name: str):
        super().__init__(name, 50)

    def breathe(self):
        self.oxygen -= self.BREATH_COST

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
