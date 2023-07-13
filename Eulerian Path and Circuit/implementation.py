# IMPLEMENTATION OF EULERIAN PATH ALGORITHIM (for reference)

def find_eulerian_path(graph):
    # Create a dictionary to store the degree of each vertex
    degrees = {}
    
    # Calculate the degree of each vertex
    for u, neighbors in graph.items():
        degree = len(neighbors)
        degrees[u] = degree
    
    # Choose a starting vertex
    start_vertex = find_start_vertex(degrees)
    
    # Initialize the stack with the starting vertex
    stack = [start_vertex]
    
    # Initialize the path
    path = []
    
    # Traverse the graph
    while stack:
        u = stack[-1]  # Get the current vertex
        
        # If there are neighbors remaining for the current vertex
        if degrees[u] > 0:
            # Choose the next neighbor
            v = graph[u].pop()
            
            # Decrement the degrees of the current vertex and the chosen neighbor
            degrees[u] -= 1
            degrees[v] -= 1
            
            # Add the chosen neighbor to the stack
            stack.append(v)
            
        # If no neighbors are remaining for the current vertex
        else:
            # Remove the current vertex from the stack and add it to the path
            path.append(stack.pop())
    
    # Reverse the path to obtain the Eulerian path
    path.reverse()
    
    return path


def find_start_vertex(degrees):
    # Find a vertex with an odd degree (if one exists)
    for vertex, degree in degrees.items():
        if degree % 2 == 1:
            return vertex
    
    # If no vertex with an odd degree is found, return any vertex
    return list(degrees.keys())[0]


# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}

eulerian_path = find_eulerian_path(graph)
print("Eulerian Path:", eulerian_path)
