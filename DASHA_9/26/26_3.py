# 26 2651 из курса
from collections import defaultdict

# читаем данные
with open('26_2651.txt') as f:
    n = int(f.readline())
    a = [tuple(map(int, line.split())) for line in f.readlines()]

d = defaultdict(set)  # словарь марок (год: марки)

kind = set(range(1, 9))  # все виды марок

for item in a:
    d[item[0]].update({item[1]})  # по ключу "год" добавляем марки в словарь (присоединяем к имеющимся)

for year, val in sorted(d.items()):
    print(year, kind.difference(val))  # пишем какой марки не хватает в текущем году

print(sum(map(lambda x: 8 - len(x), d.values())))  # сумма марок недостающих

print(max(d.keys(), key=lambda x: (8 - len(d[x]), x)))  # максимальный год

# лямбда может возвращать кортеж, таким образом даже если будет несколько годов у которых не достает одинаковое
# количество марок мы выберем наибольший год
