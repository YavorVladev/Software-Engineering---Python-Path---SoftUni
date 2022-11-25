from horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed + 2 <= self.MAX_SPEED:
            self.speed += 2
        else:
            self.speed = self.MAX_SPEED
