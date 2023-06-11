def Game(s, m, *, key=False) -> bool:
    def Rec(s, c, m) -> bool:
        if s == 42:
            return c % 2 == m % 2
        if c == m:
            return False
        if s < 42:
            t = [Rec(s + 1, c + 1, m), Rec(s + 3, c + 1, m), Rec(s + 7, c + 1, m)]
        if s > 42:
            t = [Rec(s - 1, c + 1, m), Rec(s - 3, c + 1, m), Rec(s - 7, c + 1, m)]
        if key:
            return any(t) if (c + 1) % 2 == m % 2 else any(t)
        return any(t) if (c + 1) % 2 == m % 2 else all(t)

    return Rec(s, 0, m)


# 19
for s in range(1, 42):
    if Game(s, 2):
        print(s)
        break
print('--------------------------------')
# 20
print(sorted(set(s for s in range(1, 100) if Game(s, 3)).difference(set(s for s in range(1, 100) if Game(s, 1))))[:2])

print('--------------------------------')
# 21
print(max(set(s for s in range(1, 100) if Game(s, 4)).difference(set(s for s in range(1, 100) if Game(s, 2)))))
