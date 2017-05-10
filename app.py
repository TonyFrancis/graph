from lib.graph import Graph

if __name__ == "__main__":
    oGraph = Graph()
    oGraph.addEdge("A","B")
    oGraph.addEdge("B","C")
    oGraph.addEdge("A","C")
    # print oGraph.edges
    # print list(oGraph.dfs_paths("A","B"))
    print oGraph.list_all_paths()
    # print list(oGraph.dfs_paths("B","A"))
    # print list(oGraph.dfs_paths("A","B"))
    # print list(oGraph.dfs_paths("A","C"))
    # print list(oGraph.dfs_paths("B","C"))
    # print list(oGraph.dfs_paths("C","A"))
    # print list(oGraph.dfs_paths("C","B"))
