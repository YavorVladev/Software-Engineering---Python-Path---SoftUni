n = int(input())
left_summ = 0
right_summ = 0
for i in range(1, n + 1):
    left_summ = left_summ + int(input())
for i in range(1, n + 1):
    right_summ = right_summ + int(input())

if left_summ == right_summ:
    print(f"Yes, sum = {left_summ}")
else:
    diff = abs(right_summ - left_summ)
    print(f"No, diff = {diff}")