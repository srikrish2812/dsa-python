i = 9
print(bin(i).count('1'))


import itertools

s = "abc"

for perm in itertools.permutations(s):
    print(''.join(perm))

print(1+2)
