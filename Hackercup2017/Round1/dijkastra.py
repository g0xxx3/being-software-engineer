from collections import defaultdict
int((self.node_count + 0.5) / 2)

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = self.distances[(to_node, from_node)] = distance


def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited


input_file = open('manic_moving_example_input.txt', 'r')
output_file = open('manic_moving_example_output.txt', 'w')
test_cases = int(input_file.readline())
for ts in range(1, test_cases + 1):
    input_graph = Graph()
    n, m, k = map(int, input_file.readline().split())
    for i in range(1, n + 1):
        input_graph.add_node(i)
    for i in range(m):
        a, b, g = map(int, input_file.readline().split())
        input_graph.add_edge(a, b, g)

    moves = []
    for i in range(k):
        s, d = map(int, input_file.readline().split())
        if i == 0 and s != 1:
            moves.append((1, s))  # add initial move
        moves.append((s, d))

    shortest_path = []
    for i in range(1, n+1):
        shortest_path.append(dijsktra(input_graph, i))
    print(shortest_path)
    print(moves)

    total_cost = 0
    # for i in range(len(moves)):
        # print(shortest_path[moves[i][0]])


    print('Case #{0}: {1}'.format(ts, input_graph.distances))
    # print('Case #{0}: {1}'.format(ts, input_graph.distances), file=output_file)
