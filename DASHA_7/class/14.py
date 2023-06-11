e = '0123456789abcdefghihklopm'

def f(n, m):
    s = ''
    while n > 0:
        s = e[n % m] + s
        n //= m
    return s


n = 3 * 625 ** 173 + 4 * 125 ** 180 + 3 * 25 ** 157 + 2 * 5 ** 155 + 156
k = 0
# while n > 0:
#     if n % 25 == 0:
#         k += 1
#     n //= 25
#
# print(k)

print(f(n, 25), f(n, 25).count('0'))