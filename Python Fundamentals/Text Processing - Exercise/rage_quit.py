text = input().upper()
unique_symbols = ""
current_symbols = ""
repetitions = ""
for index in range(len(text)):
    if not text[index].isdigit():
        current_symbols += text[index]
    else:
        for next_symbol in range(index, len(text)):
            if not text[next_symbol].isdigit():
                break
            repetitions += text[next_symbol]
        repetitions = int(repetitions)
        unique_symbols += repetitions * current_symbols
        current_symbols = ""
        repetitions = ""
print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)

