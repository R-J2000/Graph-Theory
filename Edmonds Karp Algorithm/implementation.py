# IMPLEMENTATION OF EDMONDS KARP ALGORITHM (for reference)

from collections import deque

def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = deque()

    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v in range(len(graph)):
            if not visited[v] and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True

    return False

def edmonds_karp(graph, source, sink):
    num_vertices = len(graph)
    parent = [-1] * num_vertices
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("inf")
        v = sink

        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u

        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow
