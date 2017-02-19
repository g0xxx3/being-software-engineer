# complexity O(mn)


def lcs(X, Y):
    m, n = len(X), len(Y)
    lcs_arr = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                lcs_arr[i][j] = lcs_arr[i-1][j-1] + 1
            else:
                lcs_arr[i][j] = max(lcs_arr[i-1][j], lcs_arr[i][j-1])


def main():
    X = "AGGTAB"
    Y = "GXTXAYB"
    print("Length of LIS is", lcs(X, Y))


if __name__ == '__main__':
    main()