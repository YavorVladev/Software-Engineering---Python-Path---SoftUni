class vowels:
    def __init__(self, letters: str):
        self.letters = letters
        self.i = 0
        self.end = len(letters) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= self.end:
            vowel = self.letters[self.i]
            self.i += 1

            if vowel in "aeiouyAEIOUY":
                return vowel
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
