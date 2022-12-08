from project.software.software import Software
from math import floor


class LightSoftware(Software):
    software_type = "Light"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, LightSoftware.software_type, floor(capacity_consumption * 1.50), floor(memory_consumption * 0.50))


