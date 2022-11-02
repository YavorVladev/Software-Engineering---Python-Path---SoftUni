delete_string = input()
main_string = input()
while delete_string in main_string:
    main_string = main_string.replace(delete_string, "")
print(main_string)