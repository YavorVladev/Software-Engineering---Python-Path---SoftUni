amount_of_floors = int(input())
amount_of_rooms = int(input())
type_of_room = ""

for current_floors in range(amount_of_floors, 0 , - 1):
    for current_rooms in range(amount_of_rooms):
        if current_floors == amount_of_floors:
            type_of_room = "L"
        elif current_floors % 2 == 0:
            type_of_room = "O"
        else:
            type_of_room = "A"
        print(f"{type_of_room}{current_floors}{current_rooms}", end=" ")
    print()