from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertices = set()
        self.adjacent_list = defaultdict(set)

    def add_edge(self, from_node, to_node):
        self.vertices.add(from_node)
        self.vertices.add(to_node)

        self.adjacent_list[from_node].add(to_node)
        self.adjacent_list[to_node].add(from_node)

    def breadth_first_search(self, source):
        level = defaultdict()
        level[source] = 0

        i = 1
        frontier = [source]
        while frontier:
            next_vertices = []
            for u in frontier:
                for v in self.adjacent_list[u]:
                    if v not in level:
                        level[v] = i
                        next_vertices.append(v)
            i += 1
            frontier = next_vertices
        return level


ts = int(input().strip())
for _ in range(ts):
    n, m = map(int, input().strip().split())
    graph = Graph(n)
    for _ in range(m):
        a, b = map(int, input().strip().split())
        graph.add_edge(a - 1, b - 1)
    s = int(input().strip()) - 1
    distances = graph.breadth_first_search(s)
    print(*[distances[i] for i in range(len(distances)) if i != s])
