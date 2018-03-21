# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 12:25:10 2018

@author: sankarth
"""
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v);
    
    def showAdjList(self,u):
        print(self.graph[u])
        
    def BFS(self,s):
        visited = [False]*(len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
        
        while queue:
            s = queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i] = True
    def DFSUtil(self, s, visited2):
        visited2[s] = True
        print(s)    
        for i in self.graph[s]:
            if(visited2[i]==False):
                self.DFSUtil(i,visited2)
                
    def DFS(self,s):
        visited2 = [False]*(len(self.graph))
        for i in range(len(self.graph)):
            if(visited2[i]==False):
                self.DFSUtil(s,visited2)
        
        
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
#g.showAdjList(0)
#g.showAdjList(1)
#g.showAdjList(2)
#g.showAdjList(3)
g.BFS(2)
print('\n')
g.DFS(2)