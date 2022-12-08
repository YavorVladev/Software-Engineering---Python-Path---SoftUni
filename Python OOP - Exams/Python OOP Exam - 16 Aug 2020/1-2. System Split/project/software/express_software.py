from project.software.software import Software


class ExpressSoftware(Software):
    software_type = "Express"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, ExpressSoftware.software_type, capacity_consumption, memory_consumption * 2)


