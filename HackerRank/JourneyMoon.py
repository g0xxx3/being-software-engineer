# https://www.hackerrank.com/challenges/journey-to-the-moon

from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertices = set()
        self.adj = defaultdict(set)
        self.visited = set()
        self.astronaut = []

    def create_edge(self, a, b):
        self.vertices.add(a)
        self.vertices.add(b)

        self.adj[a].add(b)
        self.adj[b].add(a)

    def dfs_visit(self, s):
        stack = [s]
        while stack:
            vertex = stack.pop()
            if vertex not in self.visited:
                self.visited.add(vertex)
                stack.extend(self.adj[vertex] - self.visited)

    def dfs(self):
        self.astronaut = []
        prev = 0
        for v in self.vertices:
            if v not in self.visited:
                self.dfs_visit(v)
                self.astronaut.append(len(self.visited) - prev)
                prev = len(self.visited)


n, i = map(int, input().strip().split())
graph = Graph()

for _ in range(i):
    x, y = map(int, input().strip().split())
    graph.create_edge(x, y)


graph.dfs()

total_pair = 0
distinct_vertices = n - sum(graph.astronaut)

for i in range(len(graph.astronaut)):
    for j in range(i + 1, len(graph.astronaut)):
        total_pair += graph.astronaut[i] * graph.astronaut[j]
    total_pair += graph.astronaut[i] * distinct_vertices

total_pair += (distinct_vertices * (distinct_vertices - 1)) // 2

print(total_pair)
