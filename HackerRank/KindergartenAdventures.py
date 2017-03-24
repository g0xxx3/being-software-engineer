n = int(input().strip())
a = [int(i) for i in input().strip().split()]

c = 0
max_count = 0
k = -1
for i in range(len(a)):
    c = 0
    t = i
    for j in range(len(a)):
        if j + t >= len(a):
            t = -j
        if a[j + t] - j < 1:
            c += 1
    if c > max_count:
        max_count = c
        k = i
    if max_count == len(a):
        break
print(k + 1)
