from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertices = set()
        self.adjacent_list = defaultdict(set)
        self.visited = set()
        self.order = []

    def add_edge(self, u, v):
        self.adjacent_list[u] = v

    def topological_sort(self):
        for v in self.vertices:
            if v not in self.visited:
                self.dfs_visit(v)

    def dfs_visit(self, s):
        stack = [s]
        inprocess_vertices = set()
        while stack:
            vertex = stack.pop()
            # check circular dependency
            if vertex in inprocess_vertices:
                return False
            inprocess_vertices.add(vertex)
            if vertex not in self.visited:
                self.visited.add(vertex)
                stack.extend(self.adj[vertex] - self.visited)


