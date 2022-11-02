def fill_the_box(*args):
    free_space = 1
    wanted_space = 0
    numbers = []
    command = ""
    for el in args:
        if isinstance(el, int):
            if command != "Finish":
                numbers.append(el)
        else:
            command = el
    cube_space_params = [int(x) for x in numbers[:3]]
    for cube in numbers[3:]:
        wanted_space += cube
    for number in cube_space_params:
        free_space *= number

    if command == "Finish":
        if free_space >= wanted_space:
            return f"There is free space in the box. You could put {free_space - wanted_space} more cubes."
        else:
            return f"No more free space! You have {abs(free_space - wanted_space)} more cubes."