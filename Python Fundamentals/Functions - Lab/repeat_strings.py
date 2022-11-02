#def multiply(str, int):
    #final_result = string * counter
    #print(final_result)


#string = input()
#counter = int(input())
#multiply(string,counter)
###############################################
string = input()
counter = int(input())

repeat_string = lambda a, b: a * b
result = repeat_string(string, counter)
print(result)


