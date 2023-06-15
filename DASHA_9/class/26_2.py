# задание 26 1257 из курса
from itertools import combinations

with open('26_1257.txt') as f:
    n = int(f.readline())
    a = [int(f.readline()) for i in range(n)]
    b = set(a)  # поиск в множестве происходит быстрее чем в списке, поэтому задача решается быстро достаточно
m = []
# use set b to find sums
for x, y in combinations(a, 2):
    if (x % 2 != y % 2) and (x + y) in b:
        m.append(x + y)

print(max(m), len(m))
