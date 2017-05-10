import unittest
from lib.graph import Graph

class TestGraph(unittest.TestCase):
    """Testing Graph Class."""

    def test_addEdges(self):
        """
        Multiple TestCase for adding Edge.

        1. Entered correctly.
        2. Both u and v not same.
        3. v not added repeatedly.
        4. Vertex get added.
        """
        oGraph = Graph()
        self.assertEqual(oGraph.vertex,[],"Vertex Not Empty")
        oGraph.addEdge("A","B")
        self.assertEqual(oGraph.vertex,["A","B"], "Vertex is not added")
        self.assertEqual(oGraph.edges, { "A" : ["B"]}, "Edge A -> B not saved")
        oGraph.addEdge("A","A")
        self.assertEqual(oGraph.vertex,["A","B"],"Vertex is not repeated")
        self.assertEqual(oGraph.edges, { "A" : ["B"]}, "Edge A -> A exists")
        oGraph.addEdge("A","B")
        self.assertEqual(oGraph.edges, { "A" : ["B"]}, "Repeated Entered")
        oGraph.addEdge("B","C")
        self.assertEqual(oGraph.edges, { "A": ["B"], "B" : ["C"]})
        self.assertEqual(oGraph.vertex,["A","B", "C"],"vertex not added properly")

if __name__ == '__main__':
    unittest.main()
