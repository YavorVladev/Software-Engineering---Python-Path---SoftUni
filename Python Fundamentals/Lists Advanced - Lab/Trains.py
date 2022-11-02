n_wagons = int(input())
command = input()
this_list = [0] * n_wagons
while not command == "End":
    params = command.split()
    action = params[0]
    if action == "add":
        people_to_add = int(params[1])
        this_list[-1] += people_to_add
    elif action == "insert":
        index = int(params[1])
        given_people = int(params[2])
        for i in range(len(this_list)):
            if i == index:
                this_list[i] += given_people
    elif action == "leave":
        index_again = int(params[1])
        people_again = int(params[2])
        for i in range(len(this_list)):
            if i == index_again:
                this_list[i] -= people_again

    command = input()
print(this_list)
