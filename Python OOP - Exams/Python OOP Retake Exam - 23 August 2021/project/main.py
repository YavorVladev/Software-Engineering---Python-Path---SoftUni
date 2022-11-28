from project.space_station import SpaceStation

space_station = SpaceStation()

print(space_station.add_astronaut("Biologist", "Yavor1"))
print(space_station.add_astronaut("Meteorologist", "Yavor2"))
print(space_station.add_astronaut("Geodesist", "Yavor3"))
print(space_station.add_planet("Mars", "item1, item2, item3"))
print(space_station.send_on_mission("Mars"))
print(space_station.report())
