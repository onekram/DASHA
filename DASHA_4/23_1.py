def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 2, y) + f(x + 4, y) + f(x + 5, y)


for y in range(32, 1000):
    if f(31, y) == 1001:
        print(y)
