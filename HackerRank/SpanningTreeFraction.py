#!/bin/python3


from collections import defaultdict
from math import inf


class Vertex:
    def __init__(self, node_id):
        self.id = node_id
        self.adjacent_vertices = defaultdict(tuple)
        self.cost = ()
        self.visited = False

    def add_neighbor(self, neighbor_vertex, cost_numer, cost_denom):
        self.adjacent_vertices[neighbor_vertex] = (cost_numer, cost_denom)

    def get_adjacent_vertices(self):
        return self.adjacent_vertices.keys()

    def set_cost(self, cost_numer, cost_denom):
        self.cost = (cost_numer, cost_denom)

    def get_cost(self):
        return self.cost

    def set_visited(self):
        self.visited = True


class Graph:
    def __init__(self):
        self.vertices = defaultdict()

    def __iter__(self):
        return iter(self.vertices.keys())

    def add_vertex(self, node):
        vertex = Vertex(node)
        self.vertices[node] = vertex
        return vertex

    def add_edge(self, from_vertex, to_vertex, cost_numer, cost_denom):
        from_node = self.add_vertex(from_vertex)
        to_node = self.add_vertex(to_vertex)
        from_node.add_neighbor(to_node, cost_numer, cost_denom)
        to_node.add_neighbor(from_node, cost_numer, cost_denom)


def find_minimum_spanning_tree(graph):
    

def main():
    number_of_vertices, number_of_edges = map(int, input().strip().split(' '))
    graph = Graph()
    for _ in range(number_of_edges):
        from_vertex, to_vertex, cost_numer, cost_demon = map(
            int, input().strip().split(' '))
        graph.add_edge(from_vertex, to_vertex, cost_numer, cost_demon)

    


main()
