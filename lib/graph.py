"""Graph class for graph representation."""


class Graph(object):
    """docstring for Grpah."""

    def __init__(self):
        """Initialize vertex and edges."""
        super(Graph, self).__init__()
        self.vertex = []
        self.edges = {}

    def addEdge(self, u, v):
        """Adding new vertex. and Check if cycle exists"""
        if u not in self.vertex:
            self.vertex.append(u)
        if v not in self.vertex:
            self.vertex.append(v)
        if u != v:
            edges_to_u = self.edges.get(u, [])
            if v not in edges_to_u:
                self.edges[u] = edges_to_u + [v]
        # github issue https://github.com/TonyFrancis/graph/issues/1
        # revert is It create Cycle.
        if self.cyclic():
            self.edges[u].remove(v)
            if not self.edges[u]:
                del self.edges[u]

    def cyclic(self):
        """Return True if the directed graph has a cycle."""
        g = self.edges
        path = set()
        visited = set()

        def visit(vertex):
            if vertex in visited:
                return False
            visited.add(vertex)
            path.add(vertex)
            for neighbour in g.get(vertex, ()):
                if neighbour in path or visit(neighbour):
                    return True
            path.remove(vertex)
            return False

        return any(visit(v) for v in g)

    def dfs_paths(self, start, goal):
        """
        DFS path which transerve full graph.

        Transerved path start from u and end in 'v' with all
        other vertex in between. ie, length of path is no of vertex.
        """
        graph = self.edges
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()

            for next in set(self.vertex) - set(path):
                if next == goal and len(path + [next]) == len(self.vertex):
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))

    def list_all_paths(self):
        """All Paths in graph is sum of dfs_path between 2 nodes."""
        paths = []
        for u in self.vertex:
            for v in self.vertex:
                if u != v:
                    paths = paths + list(self.dfs_paths(u, v))
        return paths
