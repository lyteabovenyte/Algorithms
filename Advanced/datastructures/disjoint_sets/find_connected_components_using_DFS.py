"""
    Depth-first search is the traditional way of computing connected components in 
    an undirected graph.
    it's good when the graph as static.
"""
import collections

def connected_components(nodes, edges):

    # helper function to perform depth-first search on a graph using the targeted node.
    def dfs(node, graph, visited, component):
        visited.add(node)
        component.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour, graph, visited, component)

    graph = collections.defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u) # undirected graph

    visited = set()
    components = []

    for node in nodes:
        if node not in visited:
            component = []
            dfs(node, graph, visited, component)
            components.append(component)
        
    return components

print(connected_components([0, 1, 2, 3, 4, 5, 6, 7], [(0, 1), (1, 2), (3, 4), (4, 5), (5, 6)]))
# returns [[0, 1, 2], [3, 4, 5, 6], [7]]