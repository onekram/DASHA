s = [1, 4, 67, 9, '35345', 'dgdfg', 6]
print(*map(lambda x: x > 5 if isinstance(x, int) else 'строчка', s))

print(*filter(lambda x: isinstance(x, int), s), sep='\n', end='.')