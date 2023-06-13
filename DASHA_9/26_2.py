with open('26_2650.txt') as f:
    l, m, n = [int(i) for i in f.readline().split()]
    a = [tuple(int(i) for i in line.split()) for line in f]
d = [0] * l

for item in a:
    for i in range(item[0], item[0] + item[1]):
        d[i] = 1


pros = []
k = 0
for i in d:
    if i == 0:
        k += 1
    else:
        pros.append(k)
        k = 0
pros.append(k)

print(len([i for i in pros if i >= m]), max(pros))
