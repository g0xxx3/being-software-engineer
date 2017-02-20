# complexity O(mn)


def print_lcs(X, Y, lcs_arr):
    i, j = len(X), len(Y)
    index = lcs_arr[len(X)][len(Y)]
    lcs_str = [''] * index

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif lcs_arr[i][j - 1] > lcs_arr[i - 1][j]:
            j -= 1
        else:
            i -= 1
    print(''.join(lcs_str))


def lcs(X, Y):
    m, n = len(X), len(Y)
    lcs_arr = [[0] * (n + 1) for _ in range(m + 1)]
    lcs_v = []
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                lcs_arr[i][j] = lcs_arr[i - 1][j - 1] + 1
                lcs_v.append(X[i - 1])
            else:
                lcs_arr[i][j] = max(lcs_arr[i - 1][j], lcs_arr[i][j - 1])
    print_lcs(X, Y, lcs_arr)
    return lcs_arr[m][n]


def main():
    X = "AGGTAB"
    Y = "GXTXAYB"
    print("Length of LCS is", lcs(X, Y))


if __name__ == '__main__':
    main()
