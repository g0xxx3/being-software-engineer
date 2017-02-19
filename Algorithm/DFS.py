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