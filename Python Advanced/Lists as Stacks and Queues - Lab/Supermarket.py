from collections import deque

names = input()
queue = deque()
while names != "End":
    if names == "Paid":
        print('\n'.join(queue))
        queue.clear()
    else:
        queue.append(names)

    names = input()

print(f"{len(queue)} people remaining.")