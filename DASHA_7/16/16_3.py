# 6565
import sys, time
from functools import lru_cache

sys.setrecursionlimit(30_000)

cache = {0: 0}


def f(n):
    result = cache.get(n)
    if result is None:
        if n < 9:
            result = n // 3 + n % 3
        else:
            result = f(n // 9) + f(n % 9)
        cache[n] = result
    return result

@lru_cache()
def f_1(n):
    if n < 9:
        result = n // 3 + n % 3
    else:
        result = f(n // 9) + f(n % 9)
    return result


# start = time.perf_counter()
# print(len([i for i in range(0, 9**9) if f(i) == 33]))
# print(time.perf_counter() - start)
#
# start = time.perf_counter()
# print(len([i for i in range(9 ** 7) if f_1(i) == 33]))
# print(time.perf_counter() - start)

fun = [n // 3 + n % 3 for n in range(9)]
print(fun)


# for i in range(9,9**9):
#     fun[i] = fun[i // 9] + fun[i % 9]
#     print(f'{i / 9**9 * 100}%')

def rec(x, y, k=0):
    if x > y or k == 10:
        return 0
    if x == y:
        return 1
    return rec(x + 1, y, k + 1) * 2 + rec(x + 2, y, k + 1) * 3 + rec(x + 3, y, k + 1) * 2 + rec(x + 4, y, k + 1)


print(rec(0, 33))
