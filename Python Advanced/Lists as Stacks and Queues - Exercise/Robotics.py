from collections import deque


def conventator(seconds):
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def time_to_seconds(str_time):
    hours, minutes, seconds = [int(x) for x in str_time.split(":")]
    return hours * 3600 + minutes * 60 + seconds


robot_names = input().split(";")
processing_time_dic = {}
busy_time_by_robot = {}
time = time_to_seconds(input())
items = deque()

for robot in robot_names:
    name, process_time = robot.split("-")
    processing_time_dic[name] = int(process_time)
    busy_time_by_robot[name] = -1

while True:
    command = input()
    if command == "End":
        break
    items.append(command)

while items:
    time += 1
    item = items.popleft()

    for name, busy_until in busy_time_by_robot.items():
        if time >= busy_until:
            busy_time_by_robot[name] = time + processing_time_dic[name]
            print(f"{name} - {item} [{conventator(time)}]")
            break
    else:
        items.append(item)
