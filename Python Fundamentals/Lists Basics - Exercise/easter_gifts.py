gifts_list = input().split()
command = input()
while not command == "No Money":
    params_command = command.split()
    action = params_command[0]
    if action == "OutOfStock":
        search_gift = params_command[1]
        gifts_list = [s.replace(search_gift, 'None') for s in gifts_list]
    elif action == "Required":
        gift_replacement = params_command[1]
        index = int(params_command[2])
        if len(gifts_list) >= index < len(gifts_list):
            for i in range(len(gifts_list)):
                if i == index:
                    gifts_list[i] = gift_replacement
    elif action == "JustInCase":
        repl_string = params_command[1]
        gifts_list.pop(-1)
        gifts_list.append(repl_string)

    command = input()

final_list = [x for x in gifts_list if x != "None"]
print(' '.join(final_list))
