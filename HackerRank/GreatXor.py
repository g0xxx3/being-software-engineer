# https://www.hackerrank.com/contests/w28/challenges/the-great-xor

# !/bin/python3

q = int(input().strip())
for _ in range(q):
    x = int(input().strip())
    i = 1
    a = 0
    while x > 1:
        if x & 1 == 0:
            a += i
        x >>= 1
        i *= 2
    print(a)
