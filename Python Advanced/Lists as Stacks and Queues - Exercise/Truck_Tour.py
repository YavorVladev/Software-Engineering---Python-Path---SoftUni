from collections import deque

n_pumps = int(input())
params_queue = deque()
for _ in range(n_pumps):
    params_data = [int(x) for x in input().split()]
    params_queue.append(params_data)

for attempt in range(n_pumps):
    tank = 0
    failed = False
    for fuel, distance in params_queue:
        tank += fuel

        if tank < distance:
            failed = True
            break
        else:
            tank -= distance

    if failed:
        params_queue.append(params_queue.popleft())
    else:
        print(attempt)
        break
