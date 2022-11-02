tasks = []
while True:
    command = input().split("-")
    if command[0] == "End":
        break
    priority = int(command[0])
    task = command[1]
    tasks.append((priority, task))

sorted_tasks = [x[1] for x in sorted(tasks)]
print(sorted_tasks)



