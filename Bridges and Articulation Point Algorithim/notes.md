#### Bridges and Articulation Point Algorithim

Bridges Algorithim

    Start at any node and perform a DFS traversal labeling nodes with an increasing id value as you go. Track the id and the smallest low link value.
    A low link value of a node is the smallest id reachable from that node--including itself. A bridge is found when the id of the node you are 
    comin from is less than the low link value of the nodeyour edge is going to.
    
    This approach to find the bridges will take O(V+E). This is accomplished by using the call back feature in the DFS.

Articulation Points Algorithim

To find articulation points in a graph, you can use the Depth-First Search (DFS) algorithm with some modifications. Articulation points, also known as cut vertices, are the vertices in a graph whose removal would result in the increase of the number of connected components in the graph.

Here's a step-by-step explanation of the algorithm to find articulation points:

    a. Perform a DFS traversal of the graph, starting from any arbitrary vertex.

    b. During the DFS traversal, maintain a few pieces of information for each vertex:

        i. A discovery time to track the order in which vertices are visited during the DFS.
        ii. A low time that represents the earliest discovered vertex reachable from the current vertex through a back edge or a 
            descendant of the current vertex in the DFS tree.
        iii A flag or boolean value to indicate whether the vertex is the root of the DFS tree (this is necessary for handling the 
            root vertex separately).
    c. Initialize a counter variable to keep track of the discovery time. Start the DFS traversal from the root vertex.

    d. When visiting each vertex, assign the current discovery time to it and increment the discovery time counter.

    e. Explore all the neighbors (adjacent vertices) of the current vertex that have not been visited yet.

    f. If a neighbor has not been visited, recursively visit it and update its low time based on the low times of its neighbors.

    g. After visiting all the neighbors, check if any of the following conditions hold for the current vertex:

        i. If the current vertex is the root of the DFS tree, and it has more than one child in the DFS tree, mark it as an articulation point.
        ii. If the current vertex is not the root of the DFS tree, and its low time value is greater than or equal to the discovery time 
            of the current vertex, mark it as an articulation point.
    h. Repeat steps 5 to 7 for all unvisited neighbors of the current vertex.

    i. After the DFS traversal is complete, the articulation points in the graph will be marked accordingly.

The above algorithm is an adaptation of the standard DFS algorithm, where additional information is tracked to identify articulation points. By performing this modified DFS traversal, you can identify the vertices that act as articulation points, indicating their significance in the connectivity of the graph.

It's important to note that this algorithm assumes an undirected connected graph. If the graph is disconnected, you can perform a DFS traversal from each connected component to find articulation points specific to that component.
