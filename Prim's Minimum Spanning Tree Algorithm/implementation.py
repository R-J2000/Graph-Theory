# IMPLEMENT EAGER PRIM'S ALGORITHIM 

import heapq

def prim_mst(graph):
    num_vertices = len(graph)
    
    # Initialize data structures
    mst = []  # Stores the MST edges
    visited = set()  # Set of visited vertices
    pq = []  # Indexed priority queue to store minimum weights
    distances = [float('inf')] * num_vertices  # Distances from MST to each vertex
    previous = [None] * num_vertices  # Track the previous vertex for each vertex
    
    # Start from vertex 0 (can choose any arbitrary starting vertex)
    start_vertex = 0
    
    # Set the distance of the start vertex to 0 and push it to the priority queue
    distances[start_vertex] = 0
    heapq.heappush(pq, (distances[start_vertex], start_vertex))
    
    while pq:
        # Extract the vertex with the minimum distance from the priority queue
        min_distance, min_vertex = heapq.heappop(pq)
        
        # Skip if the vertex has already been visited
        if min_vertex in visited:
            continue
        
        # Mark the vertex as visited
        visited.add(min_vertex)
        
        # If the previous vertex is not None, add the edge to the MST
        if previous[min_vertex] is not None:
            mst.append((previous[min_vertex], min_vertex))
        
        # Explore the neighbors of the current vertex
        for neighbor, weight in graph[min_vertex]:
            # Update the distance and previous vertex if a shorter path is found
            if neighbor not in visited and weight < distances[neighbor]:
                distances[neighbor] = weight
                previous[neighbor] = min_vertex
                # Push the updated distance to the priority queue
                heapq.heappush(pq, (distances[neighbor], neighbor))
    
    return mst
