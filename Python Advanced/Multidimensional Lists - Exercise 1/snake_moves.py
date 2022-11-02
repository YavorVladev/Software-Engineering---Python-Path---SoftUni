rows, columns = [int(x) for x in input().split()]
snake_word = input()

index = 0

matrix = []

for each_row in range(rows):
    elements = []
    for each_col in range(columns):
        elements.append(snake_word[index % len(snake_word)])
        index += 1
    if each_row % 2 != 0:
        print(*reversed(elements), sep="")
    else:
        print(*elements, sep="")
