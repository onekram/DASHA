def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '1' + b + '0'
    else:
        b = '11' + b + '11'
    return b


for i in range(1, 1000):
    if int(f(i), 2) > 225:
        print(int(f(i), 2))
        break


