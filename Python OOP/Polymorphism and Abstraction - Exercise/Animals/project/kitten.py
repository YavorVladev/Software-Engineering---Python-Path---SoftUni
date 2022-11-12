from project.cat import Cat


class Kitten(Cat):
    GENDER = "Female"

    def __init__(self, name: str, age: int):
        super().__init__(name, age, Kitten.GENDER)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {Kitten.GENDER} {self.__class__.__name__}"

    def make_sound(self):
        return f"Meow"
