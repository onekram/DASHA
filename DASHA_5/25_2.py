from fnmatch import fnmatch


for item in range(1017, 10 ** 10, 1017):
    if fnmatch(str(item), '2?5432*1') and '9' in str(item):
        print(item, item // 1017)
