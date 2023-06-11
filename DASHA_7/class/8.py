from itertools import product

c = product('012345', repeat=6)
s = sorted({''.join(i) for i in c if i[0] != '0' and i.count('2') == 1})
odd = '135'
# print(s)
# for el in s:
#     for i in range(0, len(el) - 1):
#         if (el[i - 1] in odd and el[i] == "2") or (el[i] == "2" and el[i + 1] in odd):
#             continue
#         else:
#             k += 1
# print(k)
k = 0
for item in s:
    i = item.index('2')
    if 1 <= i <= 4:
        if item[i - 1] not in odd and item[i + 1] not in odd:
            k += 1
    elif i == 0:
        if item[1] not in odd:
            k += 1
    else:
        if item[4] not in odd:
            k += 1

print(k)
