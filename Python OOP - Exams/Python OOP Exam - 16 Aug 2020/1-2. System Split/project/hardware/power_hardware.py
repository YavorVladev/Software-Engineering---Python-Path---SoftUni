from project.hardware.hardware import Hardware
from math import floor


class PowerHardware(Hardware):
    type_hardware = "Power"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, PowerHardware.type_hardware, floor(capacity_consumption * 0.25), floor(memory_consumption * 1.75))
