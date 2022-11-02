word = input().lower()
counter = 0
wanted_words = ["sand", "water", "fish", "sun"]
for i in wanted_words:
    counter += word.count(i)
print(counter)
