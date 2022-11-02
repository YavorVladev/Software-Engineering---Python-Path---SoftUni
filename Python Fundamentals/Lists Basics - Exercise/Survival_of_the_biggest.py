numbers = list(map(int, input().split()))
remover = [numbers.remove(min(numbers)) for _ in range(int(input()))]

print(*numbers, sep=", ")