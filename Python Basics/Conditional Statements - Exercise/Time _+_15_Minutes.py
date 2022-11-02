hours = int(input())
mins = int(input()) + 15

if mins > 59:
    hours += 1
    mins -= 60
if hours > 23:
    hours = 0
print(f"{hours}:{mins:02d}")