import re

text = input()
pattern = r"(?<=\s)(([A-Za-z0-9]+[A-Za-z\-\.\_0-9]*)@[A-Za-z\-]+(\.[A-Za-z]+)+)\b"
is_valid = re.findall(pattern, text)
for match in is_valid:
    print(match[0])
