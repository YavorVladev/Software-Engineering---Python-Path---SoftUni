class custom_range:
    def __init__(self, start: int, end: int):
        self.s = start
        self.e = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.s <= self.e:
            current = self.s
            self.s += 1
            return current
        else:
            raise StopIteration()

