class Validation:

    @staticmethod
    def delicacy_name_validator(name: str):
        if name.strip() == "":
            raise ValueError("Name cannot be null or whitespace!")

    @staticmethod
    def delicacy_price_validator(price: float):
        if price <= 0.0:
            raise ValueError("Price cannot be less or equal to zero!")

    @staticmethod
    def booth_capacity_validator(capacity: int):
        if capacity < 0:
            raise ValueError("Capacity cannot be a negative number!")

    @staticmethod
    def delicacy_duplication(delicacy_name: str, delicacy_list: list):
        if any(d.name == delicacy_name for d in delicacy_list):
            raise Exception(f"{delicacy_name} already exists!")

    @staticmethod
    def duplicity_booth_number(booth_number: int, booth_number_list: list):
        if any(b.booth_number == booth_number for b in booth_number_list):
            raise Exception(f"Booth number {booth_number} already exists!")

