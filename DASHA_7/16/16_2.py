# 6187
import sys

sys.setrecursionlimit(30_000)


def f(n):
    if n <= 2:
        return 5
    else:
        return f(n - 2) + n


print(f(23023))
