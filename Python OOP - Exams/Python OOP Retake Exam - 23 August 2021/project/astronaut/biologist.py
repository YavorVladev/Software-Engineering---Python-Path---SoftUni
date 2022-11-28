from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    BREATH_COST = 5

    def __init__(self, name: str):
        super().__init__(name, 70)

    def breathe(self):
        self.oxygen -= self.BREATH_COST

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

