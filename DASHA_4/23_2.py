def f(number, command, result_nums):
    if command > 7:
        return
    if command == 7:
        result_nums.add(number)

    f(number + 1, command + 1, result_nums)
    f(number + 5, command + 1, result_nums)
    f(number * 3, command + 1, result_nums)
    return result_nums


print(len(f(1, 0, set())))


print(bin(5)[2:])