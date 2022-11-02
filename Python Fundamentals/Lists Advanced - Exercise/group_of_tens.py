import sys
sequence_numbers = [int(x) for x in input().split(", ")]
group_size = - sys.maxsize
for number in sequence_numbers:
    if number >= group_size:
        group_size = number




