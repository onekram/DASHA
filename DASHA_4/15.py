for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not (((x & 123 != 0) or (x & 98 != 0)) <= ((x & 75 == 0) <= (x & a != 0))):
            flag = False
            break
    if flag:
        print(a)
        break
