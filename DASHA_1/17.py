with open('17_6605.txt') as f:
    s = [int(i) for i in f]


# print(s)

def Is5(x, y):
    return (x % 10 == 5) ^ (y % 10 == 5)


mx = 9985


def IsAbs(x, y):
    return abs(x ** 2 - y ** 2) <= mx ** 2


m = []
for i in range(0, len(s)-1):
    if Is5(s[i], s[i + 1]) and IsAbs(s[i], s[i + 1]):
        m.append(abs(s[i] ** 2 - s[i + 1] ** 2))
print(len(m), max(m))