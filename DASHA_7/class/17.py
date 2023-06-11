with open('17_7089.txt') as file:
    s = [int(line) for line in file]


def Is_mod(tup):
    return True if tup[0] % 111 == 8 or tup[1] % 111 == 8 else False


spec = []
for i in range(len(s) - 1):
    spec.append((s[i], s[i + 1]))

fil = list(filter(Is_mod, spec))
print(len(fil), sum(min(fil, key=lambda x: x[0] + x[1])))

# ans = []
# for i in range(len(s) - 1):
#     if Is_mod(s[i], s[i + 1]):
#         ans.append(s[i] + s[i + 1])

# print(len(ans), min(ans))
