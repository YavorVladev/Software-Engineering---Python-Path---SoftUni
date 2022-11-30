class Validation:

    @staticmethod
    def valid_fish_name(name: str, message: str):
        if name.strip() == "":
            raise ValueError(message)

    @staticmethod
    def valid_fish_species(specie: str, message: str):
        if specie.strip() == "":
            raise ValueError(message)

    @staticmethod
    def valid_fish_price(price: float, message: str):
        if price <= 0:
            raise ValueError(message)

    @staticmethod
    def valid_aquarium_name(name: str, message: str):
        if name.strip() == "":
            raise ValueError(message)


