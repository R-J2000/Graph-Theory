#### Topological Sort

An algorithm that can find the topological ordering of nodes in O(V+E) time. Topological ordering is an ordering of nodes in the directed graph where for each directed edge from node A to node B, node A appears before mode B in the ordering. Only directed acyclic graphs can have valid topological orderings. We can solve the Single Source Shortest Path (SSSP) using Topological ordering. 

Topological sort begins by picking an unvisited node. From that node deploy DFS only for other unvisited nodes. On the recursive callback (i.e having reached the maximum depth) add the current node to the topological ordering in reverse order.
