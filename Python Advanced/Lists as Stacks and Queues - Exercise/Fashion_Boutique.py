st_clothes = [int(x) for x in input().split()]
cap = int(input())
racks = 1
t_cap = cap

while st_clothes:
    piece_cl = st_clothes[-1]
    if piece_cl <= t_cap:
        st_clothes.pop()
        t_cap -= piece_cl
    else:
        racks += 1
        t_cap = cap

print(racks)