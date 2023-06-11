print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if not (not (y <= w) or (x <= z) or (not x)):
                    print(x, y, z, w)

