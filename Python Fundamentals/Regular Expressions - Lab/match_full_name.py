import re

text = input()
pattern_search = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

final = re.findall(pattern_search, text)
print(' '.join(final))
