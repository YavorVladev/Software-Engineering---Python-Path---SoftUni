import re

command = input()
pattern = r"\d+"
while True:
    if command:
        is_valid = re.findall(pattern, command)
        if is_valid:
            print(' '.join(is_valid), end=" ")
        command = input()
    else:
        break
