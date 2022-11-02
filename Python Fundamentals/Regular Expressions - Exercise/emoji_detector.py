import re

text = input()
pattern = r":{2}[A-Z][a-z]{2,}:{2}|\*{2}[A-Z][a-z]{2,}\*{2}"
matches = re.findall(pattern, text)
digit_pattern = re.findall('\d', text)
thresh_hold = 1
the_sum = 0
for dig in digit_pattern:
    thresh_hold *= int(dig)
print(f"Cool threshold: {thresh_hold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for match in matches:
    letters_only = re.findall("\w", match)
    the_sum = sum([ord(x) for x in letters_only])
    if the_sum >= thresh_hold:
        print(f"{match}")
