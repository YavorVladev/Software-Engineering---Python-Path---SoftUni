from project.hardware.hardware import Hardware
from math import floor


class HeavyHardware(Hardware):
    type_hardware = "Heavy"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, HeavyHardware.type_hardware, capacity_consumption * 2, floor(memory_consumption * 0.75))
