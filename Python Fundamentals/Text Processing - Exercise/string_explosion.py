the_string = input()
strength = 0
final_result = ""
for index in range(len(the_string)):
    if strength > 0 and the_string[index] != ">":
        strength -= 1
    elif the_string[index] == ">":
        strength += int(the_string[index+1])
        final_result += the_string[index]
    else:
        final_result += the_string[index]
print(final_result)
