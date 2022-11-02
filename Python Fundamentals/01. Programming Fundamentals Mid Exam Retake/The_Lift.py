people = int(input())
train_state = list(map(int, input().split(" ")))
for i in range(len(train_state)):
    if people > 3:
        people_in_wagon = 4 - int(train_state[i])
        people -= people_in_wagon
        train_state[i] += people_in_wagon
    else:
        train_state[i] += people
        people = 0
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif sum(train_state) != len(train_state) * 4:
    print("The lift has empty spots!")


print(' '.join([str(num) for num in train_state]))