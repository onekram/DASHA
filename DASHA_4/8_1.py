from itertools import permutations

numbers = set(''.join(i) for i in permutations('0123456789', r=6) if
              ''.join(i)[0] != '0' and (''.join(i)[-1] == '0' or ''.join(i)[-1] == '5'))

print(numbers)


def f(x):
    for index in range(len(x) - 1):
        if int(x[index]) % 2 == int(x[index + 1]) % 2:
            return False
    return True


print(len([i for i in numbers if f(i)]))
