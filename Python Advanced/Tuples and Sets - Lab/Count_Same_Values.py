all_numbers = tuple([float(x) for x in input().split()])
unique = []

for number in all_numbers:
    if number not in unique:
        unique.append(number)

for number in unique:
    number_count = all_numbers.count(number)
    print(f"{number} - {number_count} times")

