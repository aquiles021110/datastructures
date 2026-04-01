class graph:
    def __init__(self,n):
        self.N=n
        self.graph={i:[]for i in range(n)}
    def edges(self,a,b):
        self.graph[a].append(b)
    def is_cycle(self,node,visited,rec):
        #rec=recursive stack
        #recursive dfs
        visited[node]=True
        rec[node]=True
        for neighbour in self.graph[node]:
            if not visited[neighbour]:
                if self.is_cycle(neighbour,visited,rec):
                    return True
                elif rec[neighbour]:
                    return True
        rec[node]=False
        return False
    #Remove the node from recursion stack before returning
    def simple_cycle(self):
        visited=[False]*self.N
        rec=[False]*self.N
        for node in range(self.N):
            if not visited[node]:
                if self.is_cycle(node,visited,rec):
                    return True
                else:
                    return False
g=graph(4)
g.edges(0,1)
g.edges(1,2)
g.edges(2,3)
g.edges(3,0)
if g.simple_cycle:
    print('Cycle detected')
else:
    print('No cycle')