from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    portion_size = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, Gingerbread.portion_size, price)

    def details(self):
        return f"{self.__class__.__name__} {self.name}: {Gingerbread.portion_size}g - {self.price:.2f}lv."
