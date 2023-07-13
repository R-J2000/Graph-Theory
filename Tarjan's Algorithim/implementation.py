# IMPLEMENTATION OF TARJAN'S SSC ALGORITHIM

def tarjans_algorithm(graph):
    """
    Find strongly connected components in a directed graph using Tarjan's algorithm.

    Args:
        graph (dict): The graph represented as an adjacency list.

    Returns:
        list: A list of lists, where each inner list represents a strongly connected component.
    """
    # Initialize variables
    index_counter = 0  # Counter to track discovery time
    index = {}  # Stores the discovery time of each vertex
    low_link = {}  # Stores the low-link value of each vertex
    on_stack = set()  # Set to keep track of vertices on the current path
    stack = []  # Stack to store vertices in the current path
    result = []  # List to store the strongly connected components

    # Define the Tarjan's algorithm function
    def tarjan(vertex):
        nonlocal index_counter
        index[vertex] = index_counter
        low_link[vertex] = index_counter
        index_counter += 1
        stack.append(vertex)
        on_stack.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in index:
                tarjan(neighbor)
                low_link[vertex] = min(low_link[vertex], low_link[neighbor])
            elif neighbor in on_stack:
                low_link[vertex] = min(low_link[vertex], index[neighbor])

        # Check if the current vertex is a root of a strongly connected component
        if low_link[vertex] == index[vertex]:
            component = []
            while True:
                node = stack.pop()
                on_stack.remove(node)
                component.append(node)
                if node == vertex:
                    break
            result.append(component)

    # Run Tarjan's algorithm for each unvisited vertex
    for vertex in graph:
        if vertex not in index:
            tarjan(vertex)

    return result
