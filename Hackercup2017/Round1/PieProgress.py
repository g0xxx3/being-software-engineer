input_file = open('pie_progress.txt', 'r')
output_file = open('pie_progress_output.txt', 'w')
test_cases = int(input_file.readline())
for ts in range(1, test_cases + 1):
    n, m = map(int, input_file.readline().split())
    cost_list = [sorted([int(c) for c in input_file.readline().split()]) for _ in range(n)]
    index = [0] * n

    total_cost = 0
    for i in range(n):
        min_cost = 1000000000
        temp = 0
        for j in range(i + 1):
            if j < n and index[j] < m:
                cost = cost_list[j][index[j]] + (index[j] + 1) * (index[j] + 1) - index[j]*index[j]
                if cost < min_cost:
                    min_cost = cost
                    temp = j
        total_cost += min_cost
        index[temp] += 1

    print('Case #{0}: {1}'.format(ts, total_cost), file=output_file)
input_file.close()
