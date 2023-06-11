from itertools import *

c = product('0123456', repeat=5)
m = [''.join(i) for i in c]
c = []
for i in m:
    if i[0] != '0' and i.count('6') == 1:
        c.append(i)
j = []
for i in c:
    if i.count('2') * 2 + i.count('4') * 4 + i.count('6') * 6 < i.count('1') + i.count('3') * 3 + i.count('5') * 5:
        j.append(i)
print(len(j))
