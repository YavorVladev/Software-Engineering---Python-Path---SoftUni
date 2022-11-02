import math

word = input()
summ = 0
summ_max = 0
power_word = ""
list_of_vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'O', 'Y', 'I']
while word != "End of words":
    for syl in word:
        summ += ord(syl)
    if word[0] in list_of_vowels:
        summ *= len(word)
    elif word[0] not in list_of_vowels:
        summ = math.floor(summ / len(word))

    if summ > summ_max:
        summ_max = summ
        power_word = word

    summ = 0
    word = input()

if word == 'End of words':
    print(f'The most powerful word is {power_word} - {summ_max}')