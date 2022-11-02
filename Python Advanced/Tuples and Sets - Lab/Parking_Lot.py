car_amount = int(input())
car_plates = set()

for car in range(car_amount):
    state, plate = input().split(", ")
    if state == "IN":
        car_plates.add(plate)
    elif state == "OUT":
        car_plates.remove(plate)

if car_plates:
    for each_plate in car_plates:
        print(each_plate)
else:
    print('Parking Lot is Empty')
