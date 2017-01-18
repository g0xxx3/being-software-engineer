from math import inf


class Graph:
    def __init__(self, node_count):
        self.node_count = node_count
        self.nodes = set()
        self.edges = [x[:] for x in [[inf] * node_count] * node_count]
        for nc in range(node_count):
            self.edges[nc][nc] = 0

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node][to_node] = self.edges[to_node][from_node] = distance

    def shortest_path(self):
        for k in range(self.node_count):
            for i in range(self.node_count):
                for j in range(i+1, self.node_count):
                    if self.edges[i][j] > self.edges[i][k] + self.edges[k][j]:
                        self.edges[i][j] = self.edges[j][i] = self.edges[i][k] + self.edges[k][j]

        return self.edges

input_file = open('manic_moving.txt', 'r')
output_file = open('manic_moving_output.txt', 'w')
test_cases = int(input_file.readline())
for ts in range(1, test_cases + 1):
    n, m, k = map(int, input_file.readline().split())
    input_graph = Graph(n)
    for i in range(n):
        input_graph.add_node(i)
    for i in range(m):
        a, b, g = map(int, input_file.readline().split())
        input_graph.add_edge(a - 1, b - 1, g)

    moves = []
    for i in range(k):
        s, d = map(int, input_file.readline().split())
        moves.append((s - 1, d - 1))

    input_graph.shortest_path()

    total_cost = 0
    d_prev = 0
    s_prev = 0
    for i in range(len(moves) - 1):
        s1, d1 = moves[i]
        s2, d2 = moves[i + 1]
        if d_prev != s1:
            total_cost += input_graph.edges[d_prev][s1]

        cost1 = input_graph.edges[s1][s2] + input_graph.edges[s2][d1]
        cost2 = input_graph.edges[s1][d1] + input_graph.edges[d1][s2]

        if cost1 <= cost2:
            moves[i + 1] = (d1, d2)
            total_cost += cost1
        else:
            total_cost += input_graph.edges[s1][d1]
        d_prev = d1
        s_prev = s1

    if i < m:
        s1, d1 = moves[i + 1]
        if not (s1 == s_prev and d1 == d_prev):
            if d_prev != s1:
                total_cost += input_graph.edges[d_prev][s1]

            total_cost += input_graph.edges[s1][d1]

    if total_cost == inf:
        total_cost = -1

    print('Case #{0}: {1}'.format(ts, total_cost), file=output_file)
