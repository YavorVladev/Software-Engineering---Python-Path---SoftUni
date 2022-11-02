sequence_of_elements = input().split()
count_moves = 0
command = input()
while not command == "end":
    count_moves += 1
    index1 = int(command.split()[0])
    index2 = int(command.split()[1])
    if index1 == index2 or index1 < 0 or index2 < 0 or index1 >= len(sequence_of_elements) or index2 >= len(sequence_of_elements):
        sequence_of_elements.insert(int(len(sequence_of_elements) / 2), f"-{str(count_moves)}a")
        sequence_of_elements.insert(int(len(sequence_of_elements) / 2), f"-{str(count_moves)}a")
        print("Invalid input! Adding additional elements to the board")
    elif sequence_of_elements[index1] == sequence_of_elements[index2]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[index1]}!")
        x = sequence_of_elements.pop(index1)
        sequence_of_elements.remove(x)
    elif sequence_of_elements[index1] != sequence_of_elements[index2]:
        print("Try again!")
    if len(sequence_of_elements) == 0:
        print(f"You have won in {count_moves} turns!")
        break
    command = input()
if command == "end":
    print("Sorry you lose :(\n"
          f"{' '.join(sequence_of_elements)}")