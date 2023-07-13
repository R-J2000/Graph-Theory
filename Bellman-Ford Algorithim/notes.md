#### Bellman-Ford Algorithim

The Bellman-Ford algorithm is used to find the shortest paths from a single source vertex to all other vertices in a weighted directed graph. It handles graphs with negative edge weights as well, unlike some other shortest path algorithms like Dijkstra's algorithm. Here are the steps involved in the Bellman-Ford algorithm:

1. Initialize the graph:

    Set the distance of the source vertex to 0 and all other vertices to infinity.
    
    Set the predecessor of all vertices to null or undefined.

2. Relax edges repeatedly:

    Repeat the following step for a total of V-1 times, where V is the number of vertices in the graph.
    
    For each edge (u, v) in the graph:
    
        If the distance of the source vertex u plus the weight of the edge (u, v) is less than the current distance of v, 
            update the distance of v to the new shorter distance and set its predecessor to u.
        
3. Check for negative-weight cycles:

    Repeat the following step for each edge (u, v) in the graph.
    
    If the distance of the source vertex u plus the weight of the edge (u, v) is less than the current distance of v, 
    then there is a negative-weight cycle in the graph. This means that the algorithm cannot produce a correct result because 
    the shortest path does not exist due to the cycle.

4. Extract the shortest paths:

    After completing the V-1 iterations, the shortest paths from the source vertex to all other vertices have been found.
    
    You can trace back the predecessor pointers starting from each destination vertex to reconstruct the shortest path.
    
It's important to note that the worst-case time complexity of the Bellman-Ford algorithm is O(V * E), where V is the number of vertices and E is the number of edges in the graph. This makes it less efficient than Dijkstra's algorithm, which has a time complexity of O((V + E) * log V) with a suitable data structure like a min-heap.
