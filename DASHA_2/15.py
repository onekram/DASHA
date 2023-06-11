for a in range(0, 1000):
    flag = True
    for x in range(1, 100):
        if not (((x % 2 == 0) <= (x % 13 != 0)) or (x + a >= 1000)):
            flag = False
            break
    if flag:
        print(a)
        break

