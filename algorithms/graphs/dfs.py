from helper import create_graph, GraphMatrix


def dfs(a):
    """
        Depth First Search - probably the most important algorithm for graph traversing.
    """
    print(a, end=" ")
    visited[a] = True
    for b in graph.matrix[a]:
        if not visited[b]:
            dfs(b)


if __name__ == '__main__':
    graph = create_graph()
    graph_length = len(graph.matrix)
    visited = [False for _ in range(graph_length)]

    dfs(2)

