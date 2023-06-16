# 6396 поляков

# читаем данные данные из файла
with open('26-117.txt') as f:
    k, n = [int(i) for i in f.readline().split()]
    a = [tuple(map(int, line.split())) for line in f.readlines()]
a.sort()

d = {room: 0 for room in range(1, k + 1)}
waiting = []
last = []
for item in a:
    if min(d.values()) > item[1]:  # если чел съедет позже чем освободится ближайший - скип
        continue
    if min(d.values()) < item[0]:  # не надо ждать
        num = min(d.keys(), key=lambda x: (d[x], -x))  # выбираем с самым большим временем простоя
    else:  # надо ждать
        num = min(d.keys(), key=lambda x: (d[x], -x))
        waiting.append(d[num] - item[0] + 1)  # записываем время ожидания

    d[num] = item[1] + 30  # добавляем в словарь время освобождения + уборка
    last.append(num)
print(waiting, last)
# из-за последнего добавленного элемента ответ не сходится, не пон где ошибка
