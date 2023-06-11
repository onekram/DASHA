from itertools import permutations

c = permutations("ODECOLON", r=8)
s = {''.join(i) for i in c}


def Is(x):
    flag = True
    for i in range(len(x) - 1):
        if x[i] == x[i + 1]:
            flag = False
            break
    return flag


k = 0
for i in s:
    if Is(i):
        k += 1
print(k)
