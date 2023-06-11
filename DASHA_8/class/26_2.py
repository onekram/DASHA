# 6092
from collections import defaultdict

with open('../26-101.txt') as f:
    n, k = [int(i) for i in f.readline().split()]
    r = set([int(i) for i in f])

d = defaultdict(list)
while r:
    x = sorted(r, reverse=True)[0]
    z = x
    for i in sorted(r, reverse=True):
        if z - i >= k:
            d[x].append(i)
            z = i
    d[x].append(x)
    r.difference_update(set(d[x]))
print(len(d), max(map(len, d.values())))
# print(*[f'{key}: {val}' for key, val in d.items()], sep='\n')