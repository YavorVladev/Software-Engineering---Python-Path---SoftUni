n = int(input())
the_list = []
for i in range(n):
    the_list.append(input())
a = set(the_list)
for name in a:
    print(name)
