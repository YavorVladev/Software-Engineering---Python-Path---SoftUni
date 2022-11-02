n = int(input())
for i in range(n):
    current_word = input()
    if "," in current_word or "." in current_word or "_" in current_word:
        print(f"{current_word} is not pure!")
        continue
    print(f"{current_word} is pure.")
