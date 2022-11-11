from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, refuel: float):
        pass


class Car(Vehicle):
    AC_BONUS = 0.9

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__()
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: float):
        consumption = (self.fuel_consumption + Car.AC_BONUS) * distance

        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption

    def refuel(self, refuel: float):
        self.fuel_quantity += refuel


class Truck(Vehicle):
    AC_BONUS = 1.6

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__()
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: float):
        consumption = (self.fuel_consumption + Truck.AC_BONUS) * distance

        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption

    def refuel(self, refuel: float):
        self.fuel_quantity += refuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

