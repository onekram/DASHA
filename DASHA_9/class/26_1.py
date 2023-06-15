with open('26_838.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
    a.sort()  # по возрастанию

d1 = []
d2 = []
while a:
    d1.append(a.pop(-1))
    while sum(d2) <= sum(d1):
        d2.append(a.pop(0))

print(len(d1))
print(len(d2))

