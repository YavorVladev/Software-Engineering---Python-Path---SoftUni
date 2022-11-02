import sys
n1 = int(input())
n2 = int(input())
n3 = int(input())
largest_num = - sys.maxsize

if n1 > n2 and n1 > n3:
    largest_num = n1
elif n2 > n1 and n2 > n3:
    largest_num = n2
elif n3 > n1 and n3 > n2:
    largest_num = n3
print(f"{largest_num}")
