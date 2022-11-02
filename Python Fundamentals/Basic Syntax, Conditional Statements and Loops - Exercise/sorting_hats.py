command = input()
while command != "Welcome!":
    name = command
    if command == "Voldemort":
        print("You must not speak of that name!")
        quit()
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")
    command = input()
print("Welcome to Hogwarts.")
