from itertools import permutations

words = set(''.join(letter) for letter in permutations('ZERKKKKALO', r=6) if ''.join(letter).count('K') > 0)

print(len(words))
