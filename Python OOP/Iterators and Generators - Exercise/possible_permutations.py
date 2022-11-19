from itertools import permutations


def possible_permutations(sequence):
    result = permutations(sequence)

    for permutation in result:
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]
