from horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed + 3 <= self.MAX_SPEED:
            self.speed += 3
        else:
            self.speed = self.MAX_SPEED
