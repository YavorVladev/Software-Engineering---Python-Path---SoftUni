def char_strings(c1,c2):
    my_list = []
    result = ""
    for characters in range(ord(c1) + 1, ord(c2)):
        my_list.append(chr(characters))
        result = " ".join(my_list)
    return result


char1 = input()
char2 = input()
print(char_strings(char1, char2))


