n = int(input())
odd_sum = 0
even_sum = 0
sum = 0


for i in range(1, n+1):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

diff = abs(odd_sum - even_sum)
sum = even_sum - diff


if odd_sum == even_sum:
    print(f"Yes")
    print(f"Sum = {sum}")
else:
    print(f"No")
    print(f"Diff = {diff}")