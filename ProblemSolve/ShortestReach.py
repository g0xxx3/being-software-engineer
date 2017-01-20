# https://www.hackerrank.com/challenges/bfsshortreach

from collections import defaultdict


class Graph:
    def __init__(self, vertices_count):
        self.vertices_count = vertices_count
        self.visited = set()
        self.vertices = [i for i in range(self.vertices_count)]
        self.adjacent_list = defaultdict(set)

    def add_edge(self, from_node, to_node):
        self.adjacent_list[from_node].add(to_node)
        self.adjacent_list[to_node].add(from_node)

    def breadth_first_search(self, source):
        weight = [-1] * self.vertices_count
        weight[source] = 0
        self.visited.add(source)

        i = 6
        frontier = [source]
        while frontier:
            next_candidate = []
            for u in frontier:
                for v in self.adjacent_list[u]:
                    if v not in self.visited:
                        self.visited.add(v)
                        weight[v] = i
                        next_candidate.append(v)
            i += 6
            frontier = next_candidate
        return weight


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
