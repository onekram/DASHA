digits = '0123456789abcdef'

from functools import reduce


def to_8(x):
    s = ''
    while x > 0:
        s = str(x % 8) + s
        x //= 8
    return s


def get_even(x):
    k = 0
    for digit in x:
        if int(digit) % 2 == 0:
            k += 1
    return True if k <= 2 else False


# for x in digits:
#     s = int(f'8569{x}', 16) + int(f'12{x}48', 16)
#     s_8 = to_8(s)
#     if get_even(s_8):
#         print(s_8)

list_of = filter(get_even, map(to_8, [int(f'8569{x}', 16) + int(f'12{x}48', 16) for x in digits]))

list_of_x = filter(lambda x: get_even(to_8(int(f'8569{x}', 16) + int(f'12{x}48', 16))), digits)

print(*list_of_x)
