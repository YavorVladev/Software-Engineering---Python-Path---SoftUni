start_n = int(input())
end_n = int(input())
current_string = ""
for i in range(start_n, end_n + 1):
    current_string += chr(i) + " "
print(current_string)