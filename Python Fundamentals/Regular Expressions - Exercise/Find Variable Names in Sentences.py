import re

text = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
is_valid = re.findall(pattern, text)
print(','.join(is_valid))