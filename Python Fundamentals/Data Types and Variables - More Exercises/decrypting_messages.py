key = int(input())
n_lines = int(input())
message = []
secret_msg = ""
while n_lines > 0:
    for i in range(n_lines):
        key_to_str = chr(key)
        lower = input()
        message.append(ord(lower) + ord(key_to_str))
        n_lines -=1
        if n_lines == 0:
            break
        upper = input()
        message.append(ord(upper) + ord(key_to_str))
        n_lines -=1
        if n_lines == 0:
            break
for e in message:
    secret_msg += chr(e)
print(secret_msg)
