
def min_cost(cost, m, n):
    r = len(cost)
    c = len(cost[0])
    tc = [[0 for _ in range(c)] for _ in range(r)]

    tc[0][0] = cost[0][0]

    for i in range(1, m + 1):
        tc[i][0] = tc[i-1][0] + cost[i][0]

    for j in range(1, n + 1):
        tc[0][j] = tc[0][j-1] + cost[0][j]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = min(tc[i - 1][j - 1], tc[i][j-1], tc[i-1][j]) + cost[i][j]

    return tc[m][n]


def main():
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    print(min_cost(cost, 2, 2))


if __name__ == '__main__':
    main()
