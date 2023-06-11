with open('17-10.txt') as f:
    s = [int(i) for i in f]


def IsUnic(a, b):
    s = a + b
    return len(str(s)) == 3 and  s % 10 > (s % 100 - s % 10) // 10
m = []
for item in range(len(s) - 2):
    if IsUnic(s[item], s[item + 1]):
        m.append(s[item]+ s[item + 1])

print(len(m))
print(min(m))