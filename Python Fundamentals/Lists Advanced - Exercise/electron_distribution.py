number_of_electrons = int(input())
my_list = []
shell_position = 0

while number_of_electrons > 0:
    shell_position += 1
    max_capacity = 2 * (shell_position ** 2)
    if number_of_electrons >= max_capacity:
        my_list.append(max_capacity)
        number_of_electrons -= max_capacity
    else:
        my_list.append(number_of_electrons)
        number_of_electrons = 0
print(my_list)

