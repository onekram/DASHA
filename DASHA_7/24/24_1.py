# из пробника
with open('24_5677.txt') as file:
    s = file.readline()

s = s.replace('DAD', '***')
s = s.replace('DA', '**')
s = s.replace('AD', '**')
s = s.replace('D', '*')

k = 0
km = 0

for i in s:
    if i == '*':
        k += 1
        km = max(k, km)
    else:
        k = 0

print(km)
