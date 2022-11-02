def is_validated(string):
    is_valid = True
    if len(string) < 6 or len(string) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not string.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    counter = 0
    for character in string:
        if character.isdigit():
            counter += 1
    if counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid


password = input()
is_valid = is_validated(password)
if is_valid:
    print("Password is valid")







