string = input().split(", ")
beggars = int(input())
string_to_digits = []
index_counter = 0
final_list = []
for i in string:
    string_to_digits.append(int(i))
while index_counter < beggars:
    beggar_sum = 0
    for index in range(index_counter, len(string_to_digits), beggars):
        beggar_sum += string_to_digits[index]
    index_counter += 1
    final_list.append(beggar_sum)
print(final_list)



