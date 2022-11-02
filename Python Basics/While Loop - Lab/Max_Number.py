import sys

max_num = - sys.maxsize
command = input()

while command != "Stop":
    current_numb = int(command)
    if current_numb > max_num:
        max_num = current_numb
    command = input()
print(max_num)