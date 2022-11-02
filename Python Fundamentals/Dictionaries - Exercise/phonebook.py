phone_book = {}
while True:
    entry = input()
    if not "-" in entry:
        break
    name, phone = entry.split("-")
    phone_book[name] = phone
for validator in range(int(entry)):
    search_contact = input()
    if search_contact in phone_book:
        print(f"{search_contact} -> {phone_book[search_contact]}")
    else:
        print(f"Contact {search_contact} does not exist.")
