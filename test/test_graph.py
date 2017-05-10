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
        5. Donot Add Cyclic Edges.
        """
        oGraph = Graph()
        self.assertEqual(oGraph.vertex, [], "Vertex Not Empty")
        oGraph.addEdge("A", "B")
        self.assertEqual(oGraph.vertex, ["A", "B"], "Vertex is not added")
        self.assertEqual(oGraph.edges, {"A": ["B"]}, "Edge A -> B not saved")
        oGraph.addEdge("A", "A")
        self.assertEqual(oGraph.vertex, ["A", "B"], "Vertex is not repeated")
        self.assertEqual(oGraph.edges, {"A": ["B"]}, "Edge A -> A exists")
        oGraph.addEdge("A", "B")
        self.assertEqual(oGraph.edges, {"A": ["B"]}, "Repeated Entered")
        oGraph.addEdge("B", "C")
        self.assertEqual(oGraph.edges, {"A": ["B"], "B": ["C"]})
        self.assertEqual(oGraph.vertex, ["A", "B", "C"],
                         "vertex not added properly")
        oGraph.addEdge("C", "B")
        print oGraph.cyclic()
        self.assertEqual(oGraph.edges, {"A": ["B"], "B": ["C"]},
                         "Cyclic Edge added")

    def test_dfs_paths(self):
        """
        Test DFS paths.

        1. Should have length equal to vertex.
        2. Starting element is 'u' and ending in 'v'.
        """
        oGraph = Graph()
        self.assertEqual(list(oGraph.dfs_paths("A", "B")), [], "No Path")
        oGraph.addEdge("A", "B")
        paths = list(oGraph.dfs_paths("A", "B"))
        self.assertEqual(len(paths), 1, "Single path from A to B")
        self.assertEqual(len(paths[0]), 2,
                         "length of path is equal to no of vertex")
        self.assertEqual(paths[0][0], "A", "Starts from A")
        self.assertEqual(paths[0][-1], "B", "Ends at B")
        oGraph.addEdge("A", "C")
        paths = list(oGraph.dfs_paths("A", "B"))
        self.assertEqual(len(paths), 1, "Single path from A to B")
        self.assertEqual(len(paths[0]), 3,
                         "length of path is equal to no of vertex")
        self.assertEqual(paths[0][0], "A", "Starts from A")
        self.assertEqual(paths[0][-1], "B", "Ends at B")
        oGraph.addEdge("A", "D")
        paths = list(oGraph.dfs_paths("A", "B"))
        self.assertEqual(len(paths), 2,
                         "Single path from A to B,'ACDB','ADCB'")
        self.assertEqual(len(paths[0]), 4,
                         "length of path is equal to no of vertex")
        self.assertEqual(paths[0][0], "A", "Starts from A")
        self.assertEqual(paths[0][-1], "B", "Ends at B")

    def test_cyclic(self):
        """
        Test Cyclic Graph function.

        DAG is not cyclic. so it should always return False.
        TestCase.
        1. A -> B, A-> C Not cycle
        2. A -> B, B -> A Cycle
        3. A -> B, B -> C, C -> A Cycle
        4. A -> B, B -> C, D -> A Not Cycle.
        5. A -> A Cycle
        """
        oGraph = Graph()
        oGraph.edges = {"A": ["B", "C"]}
        self.assertFalse(oGraph.cyclic())
        oGraph.edges = {"A": ["B", "C"], "B": ["A"]}
        self.assertTrue(oGraph.cyclic(), "Graph is cyclic")
        oGraph.edges = {"A": ["B", "C"], "B": ["C"], "C": ["A"]}
        self.assertTrue(oGraph.cyclic(), "Graph is cyclic")
        oGraph.edges = {"A": ["A"]}
        self.assertTrue(oGraph.cyclic(), "Graph is cyclic")
        oGraph.edges = {"A": ["B", "C"], "B": ["C"], "D": ["A"]}
        self.assertFalse(oGraph.cyclic())


if __name__ == '__main__':
    unittest.main()
