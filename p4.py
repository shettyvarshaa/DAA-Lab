class Graph:
    def __init__(self, V):
        self.V = V
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def kruskal(self):
        self.edges.sort(key=lambda x: x[2])
        parent = list(range(self.V))
        mst = []

        def find(v):
            return v if parent[v] == v else find(parent[v])

        for u, v, weight in self.edges:
            if find(u) != find(v):
                mst.append((u, v, weight))
                parent[find(u)] = find(v)

        return mst

# Example usage
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 20)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 8)

minimum_spanning_tree = g.kruskal()

print("Minimum Spanning Tree:")
for u, v, w in minimum_spanning_tree:
    print(f"Edge: {u} - {v}, Weight: {w}")