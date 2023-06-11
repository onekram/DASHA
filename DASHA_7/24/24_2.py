# 6554
with open('24-260.txt') as file:
    s = file.readline()


k = 0
km = 0

for i in range(len(s)):
    if s[i].isdigit() and s[i + 1].isdigit() and int(s[i]) % 2 != int(s[i + 1]) % 2:
        k = 1
    else:
        k += 1
        km = max(k, km)


print(km)
