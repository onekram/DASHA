# 26 2480 из курса

# читаем данные
with open('26_2480.txt') as f:
    n = int(f.readline())
    a = [tuple(map(int, line.split())) for line in f.readlines()]

d = [0] * 2_000_000

for item in a:  # заполняем единицами там где жалоба
    for i in range(item[0], item[1]):
        d[i] = 1
k = 0
last = 0
for i in d:  # считаем количество переходов 0-1 1-0 и делим на 2 - это количесвто непрерывных участков 1
    if i != last:
        k += 1
    last = i
print(k // 2)

print(sum(d))  # длина ремонтируемых участков
