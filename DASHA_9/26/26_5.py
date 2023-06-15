# 6396 поляков

with open('26-117.txt') as f:
    k, n = [int(i) for i in f.readline().split()]
    a = [tuple(map(int, line.split())) for line in f.readlines()]
a.sort()

d = {room: 0 for room in range(1, k + 1)}
waiting = []
last = []
for item in a:
    if min(d.values()) > item[1]:
        continue
    if min(d.values()) < item[0]:
        num = max(d.keys(), key=lambda x: (item[0] - d[x], x))
    else:
        num = min(d.keys(), key=lambda x: d[x])
        waiting.append(d[num] - item[0] + 1)

    d[num] = item[1] + 30
    last.append(num)
print(waiting, last)
# из-за последнего добавленного элемента ответ не сходится, не пон где ошибка
