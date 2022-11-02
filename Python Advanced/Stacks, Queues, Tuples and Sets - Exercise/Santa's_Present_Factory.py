from collections import deque

box_materials = deque(map(int, input().split()))
magic_values = deque(map(int, input().split()))

all_magic_list = [150, 250, 300, 400]
doll = 0
wooden_train = 0
teddy_bear = 0
bicycle = 0
gift_list = {}

while box_materials and magic_values:

    current_material = box_materials[-1]
    current_magic = magic_values[0]

    if current_material == 0 and current_magic == 0:
        box_materials.pop()
        magic_values.popleft()
    elif current_material == 0:
        box_materials.pop()
    elif current_magic == 0:
        magic_values.popleft()

    if current_material * current_magic == 150:
        toy = 'Doll'
        box_materials.pop()
        magic_values.popleft()
        if toy not in gift_list:
            gift_list[toy] = 1
        else:
            gift_list[toy] += 1
        doll += 1

    elif current_material * current_magic == 250:
        toy = 'Wooden train'
        box_materials.pop()
        magic_values.popleft()
        if toy not in gift_list:
            gift_list[toy] = 1
        else:
            gift_list[toy] += 1
        wooden_train += 1

    elif current_material * current_magic == 300:
        toy = 'Teddy bear'
        box_materials.pop()
        magic_values.popleft()
        if toy not in gift_list:
            gift_list[toy] = 1
        else:
            gift_list[toy] += 1
        teddy_bear += 1

    elif current_material * current_magic == 400:
        toy = 'Bicycle'
        box_materials.pop()
        magic_values.popleft()
        if toy not in gift_list:
            gift_list[toy] = 1
        else:
            gift_list[toy] += 1
        bicycle += 1

    elif current_material * current_magic < 0:
        result = current_material + current_magic
        box_materials.pop()
        magic_values.popleft()
        box_materials.append(result)

    elif current_material * current_magic > 0 and current_material * current_magic not in all_magic_list:   # TODO could be >=0
        magic_values.popleft()
        box_materials.pop()
        box_materials.append(current_material + 15)

if doll and wooden_train > 0 or teddy_bear and bicycle > 0:
    print('The presents are crafted! Merry Christmas!')
else:
    print("No presents this Christmas!")

if box_materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(box_materials))}")
if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

for key, value in sorted(gift_list.items()):
    print(f"{key}: {value}")
