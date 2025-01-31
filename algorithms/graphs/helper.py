class GraphMatrix:
    """
        Undirected graph representation
    """
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def display(self):
        for row in self.matrix:
            print(row)


def create_graph(edges: list[list[int]] = None):
    """
        Helper function to create graph
    Args:
        edges: list containing list of 2 integers representing connections

    Returns:
        GraphMatrix object
    """
    if edges:
        g = GraphMatrix(len(edges))
        for edge in edges:
            g.add_edge(edge[0], edge[1])
    else:
        g = GraphMatrix(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
    g.display()
    return g


if __name__ == '__main__':
    gr = [[0, 1], [0, 2], [1, 2], [2, 3], [5, 6], [6, 4], [6, 0]]
    create_graph(gr)
