username = input()
password = input()
login_pass = input()

while login_pass != password:
    login_pass = input()
print(f"Welcome {username}!")