n = int(input())
a = set()
b = set()
new_biggest = ""
new_biggest_number = 0
for _ in range(n):
    a.clear()
    b.clear()
    info = input().split("-")
    parameters = info[0].split(",")
    second_parameters = info[1].split(",")
    # OF THE FIRST
    first = int(parameters[0])
    second = int(parameters[1])
    # OF THE SECOND
    first_sec = int(second_parameters[0])
    second_sec = int(second_parameters[1])
    for numbers in range(first, second + 1):
        a.add(numbers)
    for numbers in range(first_sec, second_sec + 1):
        b.add(numbers)

    inter = b & a
    if len(inter) > new_biggest_number:
        new_biggest = inter
        new_biggest_number = len(inter)
    else:
        pass
new_biggest_list = list(new_biggest)
print(f"Longest intersection is {new_biggest_list} with length {new_biggest_number}")

