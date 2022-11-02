number_of_rooms = int(input())
total_chairs = 0
total_people = 0
for current_floor in range(1, number_of_rooms + 1):
    chair_room, people_room = input().split()
    difference = len(chair_room) - int(people_room)
    if difference >= 0:
        total_chairs += difference
    else:
        total_people += abs(difference)
        print(f"{abs(difference)} more chairs needed in room {current_floor}")

if total_chairs >= total_people:
    print(f"Game On, {total_chairs} free chairs left")
