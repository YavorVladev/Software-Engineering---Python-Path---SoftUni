some_file = input().split("\\")
file, file_type = some_file[-1].split(".")
print(f"File name: {file}")
print(f"File extension: {file_type}")
