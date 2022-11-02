import sys

min_num = sys.maxsize
command = input()

while command != "Stop":
    current_numb = int(command)
    if current_numb < min_num:
        min_num = current_numb
    command = input()
print(min_num)