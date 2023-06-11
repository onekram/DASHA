from itertools import permutations


def f(x):
    for index in range(len(x) - 1):
        if int(x[index]) % 2 == int(x[index + 1]) % 2:
            return False
    return True


num = set(''.join(letter) for letter in permutations('01234567', r=5) if ''.join(letter)[0] != '0' and f(''.join(letter)))
print(len(num))