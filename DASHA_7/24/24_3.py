# 6147
with open('24-250.txt') as file:
    s = file.readline()
l = s.split('.')

km = 10 ** 6
for i in range(len(l) - 5):
    km = min(km, sum(map(len, [l[i + x] for x in range(6)])) + 7)

print(km)
