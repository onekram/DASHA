# 6526

with open('../24-259.txt', 'r') as f:
    s = f.read()

s = s.replace('ATG', '1')
s = s.replace('TAA', '2')
k = s.split('2')
l = list(map(lambda x: x.split('TAA',1)[-1], k))

p = map(lambda x: x.replace('1', 'ATG'), l)
mx = max(filter(lambda x: (not 'TGA' in x) and (not 'TAG' in x), p), key=len)
print(len(mx))
# m = []
# h = ''
# flag = False
# for i in s:
#     if i == '1':
#         flag = True
#         h += i
#         continue
#     if flag and i == '2':
#         h += i
#         m.append(h)
#         h = ''
#         flag = False
#     if flag and i != '2':
#         h += i
#
# p = map(lambda x: x.replace('1', 'ATG').replace('2', 'TAA'), m)
# print(*p)
# print(*filter(lambda x: (not 'TGA' in x) and (not 'TAG' in x), p))


