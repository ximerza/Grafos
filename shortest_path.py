from Grafos import AdjListGraph


def find_shortest_path(source, graph: AdjListGraph) -> dict:
    visited = set()
    distances = {node: float('inf') for node in graph.get_nodes()}
    distances[source] = 0

    while len(visited) < len(graph.get_nodes()):
        node = min([node for node in distances.keys() if node not in visited], key=distances.get)
        visited.add(node)
        for nei in graph.get_neighbors(node):
            if nei not in visited:
                distances_nei = distances[node] + weight
                if distances_nei < distances[nei]:
                    distances[nei] = distances_nei


    return distances



if __name__ == "__main__":
    g =     AdjListGraph()
    for i in range (7):
        g.add_vertex(i)


    g.add_edge(0,1,2)
    g.add_edge(0, 2, 6)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(3, 5, 15)
    g.add_edge(3, 4, 10)
    g.add_edge(4, 5, 6)
    g.add_edge(4, 6, 2)
    g.add_edge(6, 5, 6)

    print(find_shortest_path(0,g))