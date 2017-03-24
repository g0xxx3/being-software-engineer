#!/bin/python3


n, k = map(int, input().strip().split(' '))
rQueen, cQueen = map(int, input().strip().split(' '))
rQueen, cQueen = rQueen - 1, cQueen - 1

obstacles = set()
for _ in range(k):
    rObstacles, cObstacles = map(int, input().strip().split(' '))
    obstacles.add((rObstacles - 1, cObstacles - 1))

total = 0

for r in range(rQueen + 1, n):
    if (r, cQueen) in obstacles:
        break
    total += 1

for r in range(rQueen - 1, -1, -1):
    if (r, cQueen) in obstacles:
        break
    total += 1

for c in range(cQueen + 1, n):
    if (rQueen, c) in obstacles:
        break
    total += 1

for c in range(cQueen - 1, -1, -1):
    if (rQueen, c) in obstacles:
        break
    total += 1

r = rQueen + 1
c = cQueen + 1

while r < n and c < n:
    if (r, c) in obstacles:
        break
    total += 1
    r += 1
    c += 1

r = rQueen - 1
c = cQueen - 1

while r > -1 and c > -1:
    if (r, c) in obstacles:
        break
    total += 1
    r -= 1
    c -= 1

r = rQueen - 1
c = cQueen + 1

while r > -1 and c < n:
    if (r, c) in obstacles:
        break
    total += 1
    r -= 1
    c += 1

r = rQueen + 1
c = cQueen - 1

while r < n and c > -1:
    if (r, c) in obstacles:
        break
    total += 1
    r += 1
    c -= 1

print(total)
