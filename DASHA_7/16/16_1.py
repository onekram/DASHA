# из пробника
import sys

sys.setrecursionlimit(5_000)


def f(n):
    if n <= 10:
        return n
    if n >= 10_000:
        return 1
    if n % 2 == 0:
        return n % 10 + f(n + 2)
    else:
        return f(n - 2) - (n - 1) % 10


print(f(4500) + f(5515))
