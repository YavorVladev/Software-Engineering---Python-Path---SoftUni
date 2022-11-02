def age_assignment(*args, **kwargs):
    result = ''
    sorted_names = sorted(args, key=lambda x: x[0])
    for name in sorted_names:
        for key, value in kwargs.items():
            if name.startswith(key):
                result += f"{name} is {value} years old." + '\n'
    return result