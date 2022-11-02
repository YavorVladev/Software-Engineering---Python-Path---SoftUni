from collections import deque

queue = deque()

avilable_water = int(input())

while True:
    command = input()
    if command == "Start":
        break
    queue.append(command)

while True:
    command = input()
    if command == "End":
        break
    params = command.split()
    if len(params) == 2:
        amount = int(params[1])
        avilable_water += amount
    else:
        wanted_liters = int(params[0])
        person = queue.popleft()
        if avilable_water >= wanted_liters:
            print(f"{person} got water")
            avilable_water -= wanted_liters
        else:
            print(f"{person} must wait")
print(f"{avilable_water} liters left")
