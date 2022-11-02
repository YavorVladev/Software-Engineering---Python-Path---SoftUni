n_of_char = int(input())
total_sum = 0
for i in range(n_of_char):
    character = input()
    total_sum += ord(character)
print(f"The sum equals: {total_sum}")
