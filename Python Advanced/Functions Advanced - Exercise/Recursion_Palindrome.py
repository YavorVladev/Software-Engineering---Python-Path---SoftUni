def palindrome(word: str, index: int):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    if word[index] != word[-1 - index]:
        return f"{word} is not a palindrome"

    index += 1

    return palindrome(word, index)


print(palindrome("abbbba", 0))
print(palindrome("peter", 0))