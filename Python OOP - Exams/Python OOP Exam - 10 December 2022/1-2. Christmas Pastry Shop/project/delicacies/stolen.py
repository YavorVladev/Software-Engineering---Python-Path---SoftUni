from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    portion_size = 250

    def __init__(self, name: str, price: float):
        super().__init__(name, Stolen.portion_size, price)

    def details(self):
        return f"{self.__class__.__name__} {self.name}: {Stolen.portion_size}g - {self.price:.2f}lv."
