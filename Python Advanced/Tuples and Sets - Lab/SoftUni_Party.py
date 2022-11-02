n_guests = int(input())
all_guests = []
regulars = set()
vips = set()
arrived_people = set()

for _ in range(n_guests):
    code = input()
    all_guests.append(code)

for name in all_guests:
    for ch in name:
        if ch.isdigit():
            vips.add(name)
            break
        else:
            regulars.add(name)
            break

all_people = vips | regulars
arrived = input()
while arrived != "END":
    arrived_people.add(arrived)

    arrived = input()

didnt_come = all_people - arrived_people
print(len(didnt_come))
for people in sorted(didnt_come):
    print(people)
