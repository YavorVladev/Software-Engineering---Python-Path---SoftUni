from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    def make_sound(self):
        return f"Woof!"


class Cat(Animal):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is {self.age} year old {self.gender} {self.__class__.__name__}"

    def make_sound(self):
        return f"Meow meow!"


class Kitten(Cat):
    GENDER = "Female"

    def __init__(self, name: str, age: int):
        super().__init__(name, age, Kitten.GENDER)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is {self.age} year old {Kitten.GENDER} {self.__class__.__name__}"

    def make_sound(self):
        return f"Meow"


class Tomcat(Cat):
    GENDER = "Male"

    def __init__(self, name: str, age: int):
        super().__init__(name, age, Tomcat.GENDER)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is {self.age} year old {Tomcat.GENDER} {self.__class__.__name__}"

    def make_sound(self):
        return f"Hiss"


dog = Dog("Rocky", 3, "Male")
print(dog.make_sound())
print(dog)
tomcat = Tomcat("Tom", 6)
print(tomcat.make_sound())
print(tomcat)

kitten = Kitten("Kiki", 1)
print(kitten.make_sound())
print(kitten)
cat = Cat("Johnny", 7, "Male")
print(cat.make_sound())
print(cat)
