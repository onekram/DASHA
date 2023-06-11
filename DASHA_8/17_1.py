with open('17-199.txt') as f:
    s = [int(i) for i in f]


def IsUnic(a, b, c):
    def f(x):
        return x > 0 and x % 2 == 1 and len(str(x)) == 2

    return [f(a), f(b), f(c)] == [False, True, False]

m = []
for item in range(len(s) - 2):
    if IsUnic(s[item], s[item + 1], s[item + 2]):
        m.append(s[item]+ s[item + 1]+ s[item + 2])

print(len(m))
print(max(m))