words = input().split()
palindrome = input()
all_palindromes = [x for x in words if x[::-1] == x]
len_palindromes = [x for x in all_palindromes if x == palindrome]
print(all_palindromes)
counter = (len(len_palindromes))
print(f"Found palindrome {counter} times")



