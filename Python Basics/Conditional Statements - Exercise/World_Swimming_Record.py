record_seconds = float(input())
length_m = float(input())
one_m_in_seconds = float(input())

meters_in_sec = length_m * one_m_in_seconds
seconds_slowed = length_m // 15 * 12.5
total_time = meters_in_sec + seconds_slowed
calculated_seconds = total_time - record_seconds

if total_time >= record_seconds:
    print(f"No, he failed! He was {calculated_seconds:.2f} seconds slower.")
elif total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")