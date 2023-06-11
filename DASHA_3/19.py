from functools import lru_cache


@lru_cache(None)
def Game(x, y, c, m):
    global t
    if x + y >= 60:
        return c % 2 == m % 2
    if c == m:
        return 0
    if x > y:
        t = [Game(x + 1, y, c + 1, m), Game(x + 2, y, c + 1, m), Game(x + 3, y, c + 1, m), Game(x, y * 2, c + 1, m)]
    elif x < y:
        t = [Game(x, y + 1, c + 1, m), Game(x, y + 2, c + 1, m), Game(x, y + 3, c + 1, m), Game(x * 2, y, c + 1, m)]
    elif x == y:
        t = [Game(x + 1, y, c + 1, m), Game(x + 2, y, c + 1, m), Game(x + 3, y, c + 1, m), Game(x, y + 1, c + 1, m),
             Game(x, y + 2, c + 1, m), Game(x, y + 3, c + 1, m)]
    return any(t) if (c + 1) % 2 == m % 2 else all(t)
    # return any(t) if (c + 1) % 2 == m % 2 else any(t)

    
for y in range(1, 35):
    if Game(25, y, 0, 4):
        print(y)
