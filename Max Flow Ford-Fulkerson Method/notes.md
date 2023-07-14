#### Max Flow Ford-Fulkerson Method

Terminlogy

Residual Graph - A graph the contain residual (backward) edges. Residual edges have a capacity of 0. There remaining capcity can be computed with edge.capacity - edge.flow. This ensure the remaining capacity on an edge is always non-negative, even if the flow is negative.

Augmenting Path - A path of edges in residual graph with unused capacity greater than zero from the source s to sink t. It can only flow through edges that are not fully saturated. **Max flow is achieved when there are no more augmenting paths**

Augmenting the Flow - Updating the flow values of the edges along the augmenting path. For forward edges, this means increasing the flow by the bottleneck value. When augmenting the flow along the augmenting path, you also need to decrease the flow along the residual edge (backward pointing edges) by the bottleneck value. Residual edges allow us to "undo" bad augmented paths.

The sum of the bottleneck values in each augmenting path WILL give us the max-flow.


The Ford-Fulkerson algorithm is used to find the maximum flow in a flow network, which is a directed graph with a source node and a sink node. The goal is to determine the maximum amount of flow that can be sent from the source to the sink.

Simplified explanation of the algorithm:

    a. Start with an initial flow of 0 for all edges in the network.

    b. While there is a path from the source to the sink in the residual graph (a modified version of the original graph that keeps track 
        of available capacity), do the following steps:

    c. Find a path from the source to the sink in the residual graph. This can be done using any graph traversal algorithm, such as depth-first 
        search (DFS) or breadth-first search (BFS).

    d. Determine the maximum possible flow that can be sent along this path. This is done by finding the minimum capacity of all the edges 
        in the path.

    e. Update the flow along the path by adding the maximum flow found in the previous step to each edge.

    f. Update the residual graph by subtracting the flow from the forward edges and adding the flow to the backward edges. The residual graph 
        keeps track of the remaining capacity in each edge.

    g. Repeat steps 3-6 until there are no more paths from the source to the sink in the residual graph.

    h. The maximum flow is the sum of all flows leaving the source node.

The Ford-Fulkerson algorithm terminates when there are no more augmenting paths (paths from the source to the sink with available capacity) in the residual graph. The algorithm finds the maximum flow by repeatedly finding augmenting paths and incrementing the flow along those paths until no more paths exist.

It's worth mentioning that the Ford-Fulkerson algorithm can be implemented with different path-finding strategies, such as DFS or BFS. Additionally, there are efficient variations of the algorithm, like the Edmonds-Karp algorithm, which uses BFS to find augmenting paths and guarantees a polynomial running time.
