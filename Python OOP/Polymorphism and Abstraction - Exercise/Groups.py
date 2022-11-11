class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        pass

    def __add__(self, other):
        return f"{self.name}{other.surname}"


class Group:
    def __init__(self, name: str, surname: str):
        pass
