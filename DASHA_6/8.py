from itertools import permutations

from string import ascii_lowercase

glasn = set('aeiouy')

names = set(i for i in permutations(ascii_lowercase, r=5) if len(set(i).intersection(glasn)) >= 2)



print(len(names))