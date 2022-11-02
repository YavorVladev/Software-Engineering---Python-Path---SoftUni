text = tuple(input())
a = set()
for letter in sorted(text):
    counter = text.count(letter)
    a.add(letter)

for el in sorted(a):
    counter = text.count(el)
    print(f"{el}: {counter} time/s")