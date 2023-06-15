with open('26_117.txt') as f:
    k, n = [int(i) for i in f.readline().split()]
    a = [tuple(map(int, line.split())) for line in f.readlines()]
d = [0] * 10_000
for item in a:
    for i in range(item[0], item[1] + 30 + 1):
        d[i] += 1
