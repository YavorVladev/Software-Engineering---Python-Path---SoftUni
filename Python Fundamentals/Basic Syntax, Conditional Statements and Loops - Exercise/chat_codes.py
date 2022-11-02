n = int(input())

for i in range(n):
    message = int(input())

    if message == 88:
        print(f"Hello")
    elif message == 86:
        print(f"How are you?")
    elif message != 86 and message != 88 and message < 88:
        print(f"GREAT!")
    elif message > 88:
        print(f"Bye.")
