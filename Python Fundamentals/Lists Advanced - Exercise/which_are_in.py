string1 = input().split(", ")
string2 = input().split(", ")
final_list = []
for first_element in string1:
    for second_element in string2:
        if first_element in second_element and first_element not in final_list:
            final_list.append(first_element)
            break
print(final_list)
