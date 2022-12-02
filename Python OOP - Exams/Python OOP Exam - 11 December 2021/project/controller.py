from project.validation.validation import Validation
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __get_race(self, race_name: str):
        for r in self.races:
            if r.name == race_name:
                return r

    def __get_car(self, car_type: str):
        return [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken][-1]

    def __get_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    @property
    def __car_types(self):
        return {
            "MuscleCar": MuscleCar,
            "SportsCar": SportsCar
        }

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.__car_types:
            return

        Validation.car_model_already_exists(model, self.cars)

        new_car = self.__car_types[car_type](model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        Validation.driver_name_already_exists(driver_name, self.drivers)

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        Validation.race_name_already_exists(race_name, self.races)

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        Validation.check_if_driver_exists(driver_name, self.drivers)
        Validation.check_if_car_is_available(car_type, self.cars)

        driver = self.__get_driver(driver_name)
        car = self.__get_car(car_type)

        if driver.car:
            old_model = driver.car
            old_model.is_taken = False
            driver.car = car
            return f"Driver {driver_name} changed his car from {old_model.model} to {car.model}."

        driver.car = car
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        Validation.check_if_race_exists(race_name, self.races)
        Validation.check_if_driver_exists(driver_name, self.drivers)

        driver = self.__get_driver(driver_name)
        Validation.check_if_driver_has_car(driver)

        race = self.__get_race(race_name)
        if any(driver_name == d.name for d in race.drivers):
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        Validation.check_if_race_exists(race_name, self.races)

        race = self.__get_race(race_name)
        Validation.controller_race_participants(race)

        winners = [d for d in sorted(race.drivers, key=lambda x: -x.car.speed_limit)][:3]

        output = []
        for d in winners:
            d.number_of_wins += 1
            output.append(f"Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}.")

        return "\n".join(output)
