from worker import Worker


class CareTaker(Worker):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age, salary)
