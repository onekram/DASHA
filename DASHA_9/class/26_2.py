from itertools import combinations

with open('26_1257.txt') as f:
    n = int(f.readline())
    a = [int(f.readline()) for i in range(n)]
m = []
print(a)
for x, y in combinations(a, 2):
    if (x % 2 != y % 2) and (x + y) in a:
        m.append(x + y)

print(max(m), len(m))
