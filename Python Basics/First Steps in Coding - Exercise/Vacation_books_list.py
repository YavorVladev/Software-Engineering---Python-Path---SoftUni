broi_stranici = int(input())
stranici_per_hour = int(input())
broi_dni = int(input())

calculated_hours = broi_stranici // stranici_per_hour
hours_in_a_day = calculated_hours // broi_dni
print(hours_in_a_day)