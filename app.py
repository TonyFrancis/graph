"""
Sample Graph and its path.
"""
from lib.graph import Graph

if __name__ == "__main__":
    oGraph = Graph()
    oGraph.addEdge("A", "B")
    oGraph.addEdge("B", "C")
    oGraph.addEdge("A", "C")
    oGraph.addEdge("B", "A")
    print oGraph.edges
    print oGraph.cyclic()
    print oGraph.list_all_paths()
