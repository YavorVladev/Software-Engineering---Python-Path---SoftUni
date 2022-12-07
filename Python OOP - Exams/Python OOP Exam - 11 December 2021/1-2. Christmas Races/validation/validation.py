class Validation:

    @staticmethod
    def cal_model_name(name: str):
        if len(name) < 4:
            raise ValueError(f"Model {name} is less than 4 symbols!")

    @staticmethod
    def speed_limit_validation(current_speed: int, min_speed: int, max_speed: int):
        if min_speed > current_speed or current_speed > max_speed:
            raise ValueError(f"Invalid speed limit! Must be between {min_speed} and {max_speed}!")

    @staticmethod
    def driver_name_validation(name: str):
        if name.strip() == "":
            raise ValueError(f"Name should contain at least one character!")

    @staticmethod
    def race_name_validation(name: str):
        if name.strip() == "":
            raise ValueError(f"Name cannot be an empty string!")

    @staticmethod
    def car_model_already_exists(model: str, car_list):
        if any(c.model == model for c in car_list):
            raise Exception(f"Car {model} is already created!")

    @staticmethod
    def driver_name_already_exists(name: str, driver_list):
        if any(d.name == name for d in driver_list):
            raise Exception(f"Driver {name} is already created!")

    @staticmethod
    def race_name_already_exists(race_name: str, race_list):
        if any(r.name == race_name for r in race_list):
            raise Exception(f"Race {race_name} is already created!")

    @staticmethod
    def check_if_driver_exists(driver_name: str, driver_list):
        if all(d.name != driver_name for d in driver_list):
            raise Exception(f"Driver {driver_name} could not be found!")

    @staticmethod
    def check_if_car_is_available(type_car: str, car_list: list):
        if all(c.__class__.__name__ == type_car and c.is_taken for c in car_list) or all(
                c.__class__.__name__ != type_car for c in car_list):
            raise Exception(f"Car {type_car} could not be found!")

    @staticmethod
    def check_if_race_exists(race_name, race_list):
        if all(r.name != race_name for r in race_list):
            raise Exception(f"Race {race_name} could not be found!")

    @staticmethod
    def check_if_driver_has_car(driver: object):
        if driver.car is None:
            raise Exception(f"Driver {driver.name} could not participate in the race!")

    @staticmethod
    def controller_race_participants(race: object):
        if len(race.drivers) < 3:
            raise Exception(f"Race {race.name} cannot start with less than 3 participants!")
