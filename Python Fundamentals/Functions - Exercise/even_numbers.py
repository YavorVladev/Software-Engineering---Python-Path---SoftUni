numb_as_dig = [int(i) for i in input().split()]
is_even = lambda x: x % 2 == 0
print(list(filter(is_even, numb_as_dig)))


