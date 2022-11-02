n_pieces = int(input())
book = {}
for i in range(n_pieces):
    name, composer, key = input().split("|")
    book[name] = {'COMPOSER': composer, 'KEY': key}

command = input()
while not command == "Stop":
    params = command.split("|")
    action = params[0]

    new_piece = params[1]

    if action == "Add":
        piece_composer = params[2]
        key_piece = params[3]
        if new_piece not in book:
            book[new_piece] = {'COMPOSER': piece_composer, 'KEY': key_piece}
            print(f"{new_piece} by {piece_composer} in {key_piece} added to the collection!")
        elif new_piece in book:
            print(f"{new_piece} is already in the collection!")
    elif action == "Remove":
        if new_piece in book:
            del book[new_piece]
            print(f"Successfully removed {params[1]}!")
        elif new_piece not in book:
            print(f"Invalid operation! {params[1]} does not exist in the collection.")
    elif action == "ChangeKey":
        new_key = params[2]
        if new_piece in book:
            book[new_piece]['KEY'] = new_key
            print(f"Changed the key of {new_piece} to {new_key}!")
        elif new_piece not in book:
            print(f"Invalid operation! {new_piece} does not exist in the collection.")

    command = input()

for key, value in book.items():
    print(f"{key} -> Composer: {value['COMPOSER']}, Key: {value['KEY']}")



