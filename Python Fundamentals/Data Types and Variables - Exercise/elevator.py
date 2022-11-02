from math import ceil
number_people = int(input())
capacity_elevator = int(input())
courses = 0
if capacity_elevator != 0:
    courses = ceil(number_people / capacity_elevator)
print(courses)
