# IMPLEMENTATION OF FORD FULKERSON METHOD USING DFS (for reference)

class Edge:
    def __init__(self, v1,v2, capacity,flow):
        self.from1 = v1
        self.to1 = v2
        self.capacity = capacity
        self.residual=[]
        self.flow = flow
        
        
    def isResidual(self):
        return self.capacity == 0
    
    def remaining_capacity(self):
        
        kk = self.capacity - self.flow
        print("Line 22, inside remaining capacity, kk,self.flow",kk,self.flow )
        return self.capacity - self.flow
        
    def augment(self,bottleneck):
        print("Line 24, INside Augment, self.flow,self.residual.flow,, self.from1, self.to1, self.capacity ", self.flow,self.residual.flow, self.from1, self.to1, self.capacity )
        self.flow =+ bottleneck
        self.residual.flow =- bottleneck
        #self.residual.capacity =- bottleneck
        #self.capacity =- bottleneck
        #self.residual.capacity =- bottleneck
        
        
class Graph:
    def __init__(self, numvertices):
        self.m = numvertices
        self.graph = []
        self.initialize_empty_flow_graph()
        
    def initialize_empty_flow_graph(self):
        
        for i in range(self.m):
            self.graph.append([])
            
    def add_edge(self, v1,v2,capacity,flow):
        e1 = Edge(v1,v2, capacity,flow)
        e2 = Edge(v2,v1,0,flow)
        
        e1.residual = e2
        e2.residual = e1
                self.graph[v1].append(e1)
        self.graph[v2].append(e2)
        
class ford_fulkerson:
    def __init__(self, Graph, numvertices):
        #self.n = numvertices
        self.n = numvertices
        self.s = self.n - self.n # source index
        self.t = self.n - 1  # sink index
        self.visitedToken = 0
        #self.visited = list(range(0,self.n))
        self.visited = list(range(100,n+100))
        #self.visited = list(range(-self.n, 0))
        self.minCut = [False]*self.n
        self.maxFlow = 0
        
    def solve(self,Graph):
        
        while True:
                
            print("-------Line 293---------, in solve")
            f = self.dfs(Graph, self.s, flow = float("inf"))
            print("Line 79, bottleneck value in solve", f)
            self.visitedToken = self.visitedToken+1
            self.maxFlow = self.maxFlow+f
            
            print("Line 83: self.maxFlow and F",self.maxFlow, f )
            if f == 0:
                break
            
    def dfs(self,Graph, node, flow):
        print("-----------a-------------------")
        #print()
        
        if (node == self.t):
            print("Line 92,flow", flow)
            return flow
        
        self.visited[node] = self.visitedToken
        edges = Graph.graph[node]
        for edge in edges:
            print("Line 97:Inside for loop,edge.from1,edge.to1,edge.capacity",edge.from1,edge.to1,edge.capacity)
            if (edge.remaining_capacity()>0 and self.visited[edge.to1] != self.visitedToken):
                print("Line 99:Inside if condition, for loop")
                bottleneck = self.dfs(Graph,edge.to1, min(flow, edge.remaining_capacity()))
                #flow = edge.flow
                print("Line 102, bottleneck",bottleneck)
                if (bottleneck > 0):
                    
                    edge.augment(bottleneck)
                    
                    return bottleneck
        return 0
