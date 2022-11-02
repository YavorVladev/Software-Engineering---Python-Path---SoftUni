n = [int(x) for x in input().split()]
gr_pos = 0
gr_neg = 0
for el in n:
    if el > 0:
        gr_pos += el
    else:
        gr_neg += el

print(gr_neg)
print(gr_pos)

if gr_pos > abs(gr_neg):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')
