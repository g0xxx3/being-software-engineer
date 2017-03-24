import time


def fib_recursion(n):
    if n < 3:
        return 1
    return fib_recursion(n - 1) + fib_recursion(n - 2)


def fib_loop(n):
    if n < 3:
        return 1
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, b + a

    return a


def fib_memoized(n, memo_table):
    if n in memo_table:
        f = memo_table[n]
    elif n < 3:
        f = 1
    else:
        f = fib_memoized(n - 1, memo_table) + fib_memoized(n - 2, memo_table)
        memo_table[n] = f
    return f


def fib_bottom_up(n):
    fib = {}
    for k in range(1,n+1):
        if k < 3:
            f = 1
        else:
            f = fib[k - 1] + fib[k - 2]
        fib[k] = f
    return fib[n]


number = int(input().strip())
# t1 = time.clock()
# print(fib_recursion(number))
t2 = time.clock()
# print(t2 - t1)
print(fib_loop(number))
t3 = time.clock()
print(t3 - t2)
memo = {}
print(fib_memoized(number, memo))
t4 = time.clock()
print(t4 - t3)
print(fib_bottom_up(number))
t5 = time.clock()
print(t5 - t4)
