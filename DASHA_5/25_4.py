from fnmatch import fnmatch


def f(x):
    k = 0
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            k += 1
    return k + 1


def summa(x):
    return sum([int(i) for i in str(x)])


for item in range(4019, 10 ** 10, 4019):
    if fnmatch(str(item), '1?359*0') and f(summa(item)) == 2:
        print(item, item // 4019)
