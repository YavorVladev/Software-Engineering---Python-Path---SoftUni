from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.validation.validation import Validation


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    @property
    def __get_booth_types(self):
        return {
            "Open Booth": OpenBooth,
            "Private Booth": PrivateBooth
        }

    @property
    def __get_delicacy_types(self):
        return {
            "Gingerbread": Gingerbread,
            "Stolen": Stolen
        }

    def __find_booth(self, booth_number: int):
        for b in self.booths:
            if b.booth_number == booth_number:
                return b

    def __find_delicacy(self, delicacy_name: str):
        for d in self.delicacies:
            if d.name == delicacy_name:
                return d

    def __find_suitable_booth(self, number_of_people: int):
        try:
            return [b for b in self.booths if b.is_reserved is False and b.capacity >= number_of_people][0]
        except:
            raise Exception(f"No available booth for {number_of_people} people!")

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.__get_delicacy_types:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        Validation.delicacy_duplication(name, self.delicacies)

        created_delicacy = self.__get_delicacy_types[type_delicacy](name, price)
        self.delicacies.append(created_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in self.__get_booth_types:
            raise Exception(f"{type_booth} is not a valid booth!")

        Validation.duplicity_booth_number(booth_number, self.booths)

        created_booth = self.__get_booth_types[type_booth](booth_number, capacity)
        self.booths.append(created_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        found_booth = self.__find_suitable_booth(number_of_people)
        if not found_booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        found_booth.reserve(number_of_people)
        return f"Booth {found_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        if all(b.booth_number != booth_number for b in self.booths):
            raise Exception(f"Could not find booth {booth_number}!")

        if all(d.name != delicacy_name for d in self.delicacies):
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        found_booth = self.__find_booth(booth_number)
        found_delicacy = self.__find_delicacy(delicacy_name)

        found_booth.delicacy_orders.append(found_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        found_booth = self.__find_booth(booth_number)
        total_bill = found_booth.price_for_reservation + sum([d.price for d in found_booth.delicacy_orders])
        self.income += total_bill
        found_booth.delicacy_orders = []
        found_booth.is_reserved = False
        found_booth.price_for_reservation = 0

        return f"Booth {booth_number}:\n" \
               f"Bill: {total_bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
