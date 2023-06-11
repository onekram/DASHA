def fib(n):
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def rec(x, y):
    if x == y:
        return 1
    if x > y:
        return 0

    return rec(x + 1, y) + rec(x + 4, y) + rec(x + max(filter(lambda f: f < x, [fib(i) for i in range(0, 10)])), y)


print([fib(i) for i in range(0, 10)])
print(rec(2, 16))
