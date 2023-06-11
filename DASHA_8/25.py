from fnmatch import fnmatch

for i in range(50068, 10 ** 10, 50068):
    if fnmatch(str(i), '9?979*8') and '0' in str(i):
        print(i, i // 50068)
