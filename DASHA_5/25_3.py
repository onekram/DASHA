from fnmatch import fnmatch


def f(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return 0
    return 1


s = [i for i in range(10**3, 10 ** 5) if f(i)]

for item in s:
    if fnmatch(str(item ** 2), '1?2*0*2?1'):
        print(item ** 2, item)
