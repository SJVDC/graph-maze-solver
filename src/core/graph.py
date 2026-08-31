class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, source, destination, weight=1):
        self.add_node(source)
        self.add_node(destination)

        if (destination, weight) not in self.adjacency_list[source]:
            self.adjacency_list[source].append((destination, weight))
        if (source, weight) not in self.adjacency_list[destination]:
            self.adjacency_list[destination].append((source, weight))

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def __repr__(self):
        return f"Graph with {len(self.adjacency_list)} nodes."


Grafo = Graph
