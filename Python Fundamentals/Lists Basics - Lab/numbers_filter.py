n = int(input())
my_list = []
filtered_list = []
for i in range(n):
    numbers = int(input())
    my_list.append(numbers)
command = input()
if command == "even":
    for integer in my_list:
        if integer % 2 == 0:
            filtered_list.append(integer)
elif command == "odd":
    for integer in my_list:
        if integer % 2 != 0:
            filtered_list.append(integer)
elif command == "negative":
    for integer in my_list:
        if integer < 0:
            filtered_list.append(integer)
elif command == "positive":
    for integer in my_list:
        if integer >= 0:
            filtered_list.append(integer)
print(filtered_list)
