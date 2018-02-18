# https://www.geeksforgeeks.org/dynamic-programming-set-9-binomial-coefficient/
# The binomial coefficients can be arranged to form Pascal's triangle.
# https://en.wikipedia.org/wiki/Binomial_coefficient
# c(n,k) = c(n-1, k-1) + c(n-1, k)
# base condition: c(n,0)= c(n,n) = 1


# Time Complexity : O(2^n)
# Space complexity : O(n)
def get_binomial_coefficient_recursive(n, k):
    if k == 0 or k == n:
        return 1
    return get_binomial_coefficient_recursive(n - 1, k - 1) + get_binomial_coefficient_recursive(n-1, k)


# Time Complexity: O(n*k)
# Space Complexity : O(n*k)
def get_binomial_coefficient_dp(n, k):
    c = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                c[i][j] = 1
            else:
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
    return c[n][k]


# Time Complexity: O(n*k)
# Space Complexity : O(k)
def get_binomial_coefficient_best(n, k):
    c = [0 for _ in range(k + 1)]
    c[0] = 1

    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
                c[j] = c[j] + c[j - 1]
    return c[k]


if __name__ == '__main__':
    print(get_binomial_coefficient_recursive(5, 2))
    print(get_binomial_coefficient_recursive(6, 2))
    print(get_binomial_coefficient_recursive(6, 3))
    print("")
    print(get_binomial_coefficient_dp(5, 2))
    print(get_binomial_coefficient_dp(6, 2))
    print(get_binomial_coefficient_dp(6, 3))

    print("")
    print(get_binomial_coefficient_best(5, 2))
    print(get_binomial_coefficient_best(6, 2))
    print(get_binomial_coefficient_best(6, 3))
