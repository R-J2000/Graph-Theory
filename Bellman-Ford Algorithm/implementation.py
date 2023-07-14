# IMPLEMENTATION OF BELLMAN-FORD ALGORITHM (for reference)

def bellman_ford(graph, start):
    """
    Find the shortest paths from a given start node to all other nodes in a weighted graph using the Bellman-Ford algorithm.
    
    Args:
        graph (dict): The graph represented as an adjacency list with edge weights.
        start (int): The starting node for the shortest path search.
        
    Returns:
        dict: A dictionary containing the shortest distances from the start node to all other nodes.
    """
    
    # Step 1: Initialize the distances dictionary with all distances set to infinity
    distances = {node: float('inf') for node in graph}
    
    # Set the distance of the start node to 0
    distances[start] = 0
    
    # Step 2: Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    
    # Step 3: Check for negative weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative weight cycle")
    
    return distances
