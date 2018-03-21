class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for i in range(self.V)] for j in range(self.V)]
    
    def minDistance(self,dist,spset):
        minimum = float("inf")
        for v in range(self.V):
            if(dist[v]<minimum and spset[v]==False):
                minimum = dist[v]
                min_index = v
        return min_index
    
    def printsol(self,dist):
        print(dist)
        
    def dijkstra(self,src):
        dist = [float("inf")]*self.V
        spset = [False]*self.V
        dist[src] = 0
        for count in range(self.V):
            u = self.minDistance(dist,spset)
            spset[u]=True
            for v in range(self.V):
                if(self.graph[u][v]>0 and spset[v]==False and 
                   dist[v]>dist[u]+self.graph[u][v]):
                    dist[v] = dist[u]+self.graph[u][v]
        self.printsol(dist)

g  = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]];
 
g.dijkstra(0);