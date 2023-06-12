# 6262

with open('26-109.txt') as f:
    n = int(f.readline())
    s = [int(i) for i in f]
s.sort()

m = []

for i in s:
    m.append(i)
    c = len(m) // 6
    if sum(m[:-c]) + sum(m[-c:]) // 2 > 100_000:
        m.pop(-1)
        print(len(m), 100_000 - sum(m[:-c]) - sum(m[-c:]) // 2)
        break




