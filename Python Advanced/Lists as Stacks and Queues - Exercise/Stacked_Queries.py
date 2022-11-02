from collections import deque
the_stack = deque()
amount_quries = int(input())
for x in range(amount_quries):
    command = input().split()
    if len(command) == 2:
        the_number = int(command[1])
        the_stack.appendleft(the_number)
    elif command[0] == "2":
        if len(the_stack) == 0:
            pass
        else:
            the_stack.popleft()
    elif command[0] == "3":
        if len(the_stack) == 0:
            pass
        else:
            print(max(the_stack))
    elif command[0] == "4":
        if len(the_stack) == 0:
            pass
        else:
            print(min(the_stack))

the_stack = list(map(lambda x: str(x), the_stack))

print(', '.join(the_stack))