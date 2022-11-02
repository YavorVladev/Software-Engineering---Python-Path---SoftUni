import re

text = input()
search_pattern = r'(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\b'
final = re.findall(search_pattern, text)
print(', '.join(final))