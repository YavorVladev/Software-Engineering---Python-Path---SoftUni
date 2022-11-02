import re

text = input()
pattern = r"(\||\#)([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d{1,5})\1"
is_valid = re.finditer(pattern, text)
the_list = []
cals = 0
for match in is_valid:
    exp_date = match.group(3)
    calories = match.group(4)
    items = match.group(2)
    the_list.append([items, exp_date, calories])
    cals += int(calories)
days = cals // 2000
print(f"You have food to last you for: {days} days!")
for item in the_list:
    print(f"Item: {item[0]}, Best before: {item[1]}, Nutrition: {item[2]}")

