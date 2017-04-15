# http://algorithms.tutorialhorizon.com/dynamic-programming-minimum-cost-path-problem/


def find_min_cost_path(matrix):
    n = len(matrix)
    solution = [[0] * n for _ in range(n)]
    solution[0][0] = matrix[0][0]
    for i in range(1, n):
        solution[i][0] = matrix[i][0] + solution[i - 1][0]
        solution[0][i] = matrix[0][i] + solution[0][i - 1]

    for i in range(1, n):
        for j in range(1, n):
            solution[i][j] = matrix[i][j] + min(solution[i - 1][j], solution[i][j - 1])

    return solution[n - 1][n - 1]

