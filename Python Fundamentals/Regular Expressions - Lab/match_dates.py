import re

text = input()
pattern_search = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b"
final = re.findall(pattern_search, text)
for match in final:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")