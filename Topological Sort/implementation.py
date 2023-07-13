# IMPLEMENTATION OF TOPOLOGICAL SORT (for reference)

def topological_sort(graph):
    """
    Perform topological sort on a directed acyclic graph (DAG).
    
    Args:
        graph (dict): The graph represented as an adjacency list.
        
    Returns:
        list: The sorted nodes in topological order.
    """
    
    visited = set()  # Set to track visited nodes
    stack = []  # Stack to store nodes in the order of their finishing times
    
    def dfs(node):
        """Recursive helper function for depth-first search."""
        if node in visited:
            return
        
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(neighbor)
        
        stack.append(node)
    
    # Perform DFS on each unvisited node
    for node in graph:
        dfs(node)
    
    # Reverse the order to obtain topological sort
    return stack[::-1]
