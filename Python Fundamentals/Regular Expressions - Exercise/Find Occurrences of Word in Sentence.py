import re

text = input()
wanted_word = input()
pattern = fr"\b{wanted_word}\b"
is_valid = re.findall(pattern, text, flags=re.IGNORECASE)
print(len(is_valid))
