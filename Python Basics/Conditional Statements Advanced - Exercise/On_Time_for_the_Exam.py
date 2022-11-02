exam_h = int(input())
exam_m = int(input())
exam_a_h = int(input())
exam_a_m = int(input())

exam_in_minutes = (exam_h * 60) + exam_m
ariv_in_min = (exam_a_h * 60) + exam_a_m
diff = (exam_in_minutes - ariv_in_min)

if diff < 0:
   print("Late")
   hours = abs(diff) // 60
   minutes = abs(diff) % 60
   if hours == 0:
      print(f"{minutes} minutes after the start")
   else:
      print(f"{hours}:{minutes:02d} hours after the start")

elif 0 <= diff <= 30:
   print(f"{diff} On time.")
   if diff > 0:
      print(f"{diff} minutes before the start")

elif diff > 30:
   print("Early")
   hours = abs(diff) // 60
   minutes = abs(diff) % 60
   if hours == 0:
      print(f"{minutes} minutes before the start")
   else:
      print(f"{hours}:{minutes:02d} hours before the start")