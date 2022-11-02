rows, columns = [int(x) for x in input().split()]

for row_idx in range(rows):
    for col_idx in range(columns):
        print(f"{chr(97 + row_idx)}{chr(97 + col_idx + row_idx)}{chr(97 + row_idx)}", end=" ")
    print()
