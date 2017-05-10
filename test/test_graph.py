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
        self.assertEqual(oGraph.vertex, [], "Vertex Not Empty")
        oGraph.addEdge("A", "B")
        self.assertEqual(oGraph.vertex, ["A", "B"], "Vertex is not added")
        self.assertEqual(oGraph.edges, { "A" : ["B"] }, "Edge A -> B not saved")
        oGraph.addEdge("A", "A")
        self.assertEqual(oGraph.vertex, ["A", "B"], "Vertex is not repeated")
        self.assertEqual(oGraph.edges, { "A" : ["B"]}, "Edge A -> A exists")
        oGraph.addEdge("A", "B")
        self.assertEqual(oGraph.edges, { "A" : ["B"]}, "Repeated Entered")
        oGraph.addEdge("B", "C")
        self.assertEqual(oGraph.edges, { "A": ["B"], "B" : ["C"]})
        self.assertEqual(oGraph.vertex, ["A", "B", "C"], "vertex not added properly")

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
        self.assertEqual(len(paths[0]), 2, "length of path is equal to no of vertex")
        self.assertEqual(paths[0][0], "A", "Starts from A")
        self.assertEqual(paths[0][-1], "B", "Ends at B")
        oGraph.addEdge("A", "C")
        paths = list(oGraph.dfs_paths("A", "B"))
        self.assertEqual(len(paths), 1, "Single path from A to B")
        self.assertEqual(len(paths[0]), 3, "length of path is equal to no of vertex")
        self.assertEqual(paths[0][0], "A", "Starts from A")
        self.assertEqual(paths[0][-1], "B", "Ends at B")
        oGraph.addEdge("A", "D")
        paths = list(oGraph.dfs_paths("A", "B"))
        self.assertEqual(len(paths), 2, "Single path from A to B,'ACDB','ADCB'")
        self.assertEqual(len(paths[0]), 4, "length of path is equal to no of vertex")
        self.assertEqual(paths[0][0], "A", "Starts from A")
        self.assertEqual(paths[0][-1], "B", "Ends at B")

    def check_vertex_at_begin(self, vertex, paths):
        """Check vertex present at begining of the path"""
        vertex_at_begin = False
        for path in paths:
            if path[0] == vertex:
                vertex_at_begin = True
                break;
        return vertex_at_begin

    def check_vertex_at_end(self, vertex, paths):
        """Check vertex present at end of the path"""
        vertex_at_end = False
        for path in paths:
            if path[-1] == vertex:
                vertex_at_end = True
                break;
        return vertex_at_end

    def check_path_length(self, paths, length):
        """
        check length of all path

        Path length should same as length.
        """
        for path in paths:
            if len(path) != length:
                return False
        return True

    def test_list_all_paths(self):
        """
        Test All Paths.

        1. All vertex should come in Starting and Ending of Path.
        2. All Paths should have equal length.
        """
        oGraph = Graph()
        self.assertEqual(oGraph.list_all_paths(), [], "Empty list")
        oGraph.addEdge("A", "B")
        paths = oGraph.list_all_paths()
        self.assertEqual(len(paths), 2, "there are 2 path.since only 2 vertex")
        self.assertTrue(self.check_vertex_at_begin("A", paths), "vertex A present in Begining ")
        self.assertTrue(self.check_vertex_at_begin("B", paths), "vertex B present in Begining ")
        self.assertTrue(self.check_vertex_at_end("A", paths), "vertex A present in Ending ")
        self.assertTrue(self.check_vertex_at_end("B", paths), "vertex V present in Ending ")
        self.assertTrue(self.check_path_length(paths, len(oGraph.vertex)))
        oGraph.addEdge("A", "C")
        paths = oGraph.list_all_paths()
        self.assertEqual(len(paths), 6, "there are 6 possible path")
        self.assertTrue(self.check_vertex_at_begin("A", paths), "vertex A present in Begining ")
        self.assertTrue(self.check_vertex_at_begin("B", paths), "vertex B present in Begining ")
        self.assertTrue(self.check_vertex_at_begin("C", paths), "vertex C present in Begining ")
        self.assertTrue(self.check_vertex_at_end("A", paths), "vertex A present in Ending ")
        self.assertTrue(self.check_vertex_at_end("B", paths), "vertex V present in Ending ")
        self.assertTrue(self.check_vertex_at_begin("C", paths), "vertex C present in Begining ")
        self.assertTrue(self.check_path_length(paths, len(oGraph.vertex)))

if __name__ == '__main__':
    unittest.main()
