message = input()
encrypted_message = ""
for symbol in message:
    letters = ord(symbol) + 3
    encrypted_message += chr(letters)
print(encrypted_message)