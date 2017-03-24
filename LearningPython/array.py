# a = [0, 1, 2, 3, 4, 5]
#
# print(a[1:3])  # elements except first one and upto first three
# print(a[:-2])  # elements except last two
# print(a[1:-2])  # elements except first one and last two
# b = a[:]  # shallow copy of the array
#
# a[0] = 4
# print(b)

# s = 'AABCAAADA'
# n = 3
#
# for p in zip(*[iter(s)]*3):
#     print(p)

# S, N = input(), int(input())
# for part in zip(*[iter(S)] * N):
#     d = dict()
#     print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))


# l = set({1,2,3,4})
# print(*iter(l))
#
# for i in l:
#     print(i)

# from itertools import groupby
#
# print(*[(len(list(c)), k) for k, c in groupby([1,2,2,3,4,5,1,1,3])])

from itertools import combinations

n, char_set, k = input(), input().split(), int(input())
C = list(combinations(char_set, k))
print('{0:.3}'.format(len(list(filter(lambda c: 'a' in c, C)))/len(C)))
