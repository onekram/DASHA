# 26 963 из курса


# читаем данные
with open('26_936.txt') as f:
    n, s = [int(i) for i in f.readline().split()]  # количество грузов и грузоподъемность
    a = [int(i) for i in f]  # грузы

a.sort(reverse=True)  # отсортировали по убыванию

traffic = []  # грузы
c = 0  # текущий груз (точнее его масса)

while a:  # while any cargo in a
    for i in range(len(a)):  # for
        if c + a[i] <= s:  # если влезает то запихиваем
            c += a[i]
            a[i] = 0  # убираем погруженный (метод pop здесь не сработает тк поменяется длинна а (мы по ней
            # итереируемся в форе))
    a = [i for i in a if i != 0]  # убираем все нулевые элементы, они фактически уже погружены

    traffic.append(c)  # добавляем груз
    c = 0  # обнуляем текущий груз

print(len(traffic), traffic[-1])
