#### Tarjan's Algorithim to Find Strongly Connected Components

Stack Invariant

To deal with the random traversal order of DFS, Tarjan's Algorithim maintains a stack from which low link values can be updated. Nodes are added to 
the stack of valid node ones they are explored for the first time. They are removed from the stack each time an SCC is found.

This modifies our low link update condition. To update the low link value of node u to the low link value of node v, there must be a path from u to v and v must be in the stack.

Tarjan's Algorithim Steps

Tarjan's algorithm is a popular algorithm used to find strongly connected components (SCCs) in a directed graph. It is named after its creator, Robert Tarjan. SCCs are subsets of vertices in a graph where each vertex is reachable from every other vertex within the subset.

Here are the steps of Tarjan's algorithm:

    a. Perform a depth-first search (DFS) traversal of the graph, starting from any arbitrary vertex.

    b. During the DFS traversal, assign each vertex a unique index (also known as the discovery time) and a low-link value. The discovery 
        time represents the order in which vertices are visited during the DFS, and the low-link value represents the smallest index 
        reachable from the vertex, either directly or through a sequence of back edges.

    c. Maintain a stack data structure to keep track of the vertices in the current DFS path.

    d. When visiting a vertex for the first time, assign it a discovery time and a low-link value, and push it onto the stack.

    e. Explore all the neighbors (adjacent vertices) of the current vertex that have not been visited yet.

    f. If a neighbor has not been visited, recursively visit it and update its low-link value based on the low-link values of its neighbors.

    g. After visiting all the neighbors, check if the low-link value of the current vertex is equal to its discovery time. If it is, 
        it indicates that the current vertex is the root of a strongly connected component.

    h. Pop vertices from the stack until the current vertex is reached. The popped vertices form a strongly connected component.

    i. Repeat steps 4 to 8 for all unvisited vertices in the graph until all SCCs are identified.

Tarjan's algorithm efficiently identifies SCCs using the stack and the low-link values. By maintaining the stack invariant (where vertices on the current DFS path remain on the stack until the end of their respective SCCs is reached), it avoids revisiting vertices that have already been processed and ensures that the SCCs are correctly identified.

The SCCs identified by Tarjan's algorithm provide valuable insights into the structure and connectivity of directed graphs. They are useful in various applications, such as analyzing social networks, detecting cycles in dependency graphs, and optimizing compiler designs.
