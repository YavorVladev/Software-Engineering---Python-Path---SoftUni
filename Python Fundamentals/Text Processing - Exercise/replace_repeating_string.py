my_string = input()
counter = 0
extra = []
last_char = my_string[-1]
for index in range(len(my_string) - 1):
    if my_string[index] == my_string[index+1]:
        continue
    extra.append(my_string[index])
print(''.join(extra) + last_char)
