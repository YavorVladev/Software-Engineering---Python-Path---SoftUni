input_command = input()
total_tickets = 0
standard_counter = 0
student_counter = 0
kid_counter = 0

while input_command != "Finish":
    movie = input_command
    free_space = int(input())

    ticket_counter = 0
    command_line = input()
    while command_line != "End":
        type_ticket = command_line
        if type_ticket == "standard":
            standard_counter += 1
        elif type_ticket == "student":
            student_counter += 1
        else:
            kid_counter += 1

        ticket_counter += 1
        total_tickets += 1
        if ticket_counter == free_space:
            break
        command_line = input()

    percent_full = ticket_counter / free_space * 100
    print(f"{movie} - {percent_full:.2f}% full.")

    input_command = input()

stud_tick_avg = student_counter / total_tickets * 100
stan_tick_avg = standard_counter / total_tickets * 100
kids_tick_avg = kid_counter / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{stud_tick_avg:.2f}% student tickets.")
print(f"{stan_tick_avg:.2f}% standard tickets.")
print(f"{kids_tick_avg:.2f}% kids tickets.")