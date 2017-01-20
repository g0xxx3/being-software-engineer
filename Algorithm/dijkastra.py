from collections import defaultdict
from math import inf
from queue import PriorityQueue


class Graph:
    def __init__(self):
        self.vertices = set()
        self.adjacencies = defaultdict(set)
        self.distances = {}

    def add_edge(self, from_node, to_node, distance):
        self.vertices.add(from_node)
        self.vertices.add(to_node)

        self.adjacencies[from_node].add(to_node)
        self.adjacencies[to_node].add(from_node)

        self.distances[(from_node, to_node)] = self.distances[(to_node, from_node)] = distance

    def dijsktra(self, source):
        weights = defaultdict()
        priority_queue = PriorityQueue()

        for v in self.vertices:
            if v == source:
                weights[v] = 0
            else:
                weights[v] = inf
            priority_queue.put(v)

        path = []
        while not priority_queue.empty():
            u = priority_queue.get()
            path.append(u)
            for v in self.adjacencies[u]:
                if weights[v] > weights[u] + self.distances[(u, v)]:
                    weights[v] = weights[u] + self.distances[(u, v)]

        return path


n, m, k = map(int, input().strip().split())
graph = Graph()

for _ in range(k):
    input()
for _ in range(m):
    a, b, d = map(int, input().strip().split())
    graph.add_edge(a - 1, b - 1, d)

print(graph.dijsktra(0))
