s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
n = int(input())
num_set = set()

for _ in range(n):
    params = input().split()
    command = params[0]
    place = params[1]
    new_len = len(params) - 2

    if command == "Add" and place == "First":
        params.reverse()
        for idx in range(new_len):
            s1.add(int(params[idx]))

    elif command == "Add" and place == "Second":
        params.reverse()
        for idx in range(new_len):
            s2.add(int(params[idx]))
    elif command == "Remove" and place == "First":
        params.reverse()
        for idx in range(new_len):
            if int(params[idx]) in s1:  # TODO add else if not 100 / 100
                s1.remove(int(params[idx]))
    elif command == "Remove" and place == "Second":
        params.reverse()
        for idx in range(new_len):
            if int(params[idx]) in s2:  # TODO add else if not 100 / 100
                s2.remove(int(params[idx]))
    elif command == "Check" and place == "Subset":
        if s2 < s1 or s1 < s2:   # TODO might throw an error
            print("True")
        else:
            print("False")
print(*sorted(s1), sep=", ")
print(*sorted(s2), sep=", ")