class graph:
    def __init__(self,n):
        self.n=n
        self.adj=[[] for i in range(n)]
    def edge(self,x,y):
        self.adj[x-1].append(y-1) 
        #this instruction will add y as a neighbour of x
        self.adj[y-1].append(x-1)
        #this instruction will add x as a neighbour of y 
    def search(self,source):
        visited=[False]*self.n
        result=[]
        queue=[]
        queue.append(source)
        visited[source]=True
        while len(queue)>0:
            s=queue.pop(0)
            result.append(s)
            for node in self.adj[s]:
                if visited[node]==False:
                    queue.append(node)
                    visited[node]=True
        return result
    def degree(self, node):
        return len(self.adj[node-1])
graph=graph(5)
graph.edge(1,2)
graph.edge(1,3)
graph.edge(2,4)
print(graph.search(0))
print(graph.degree(2))
#finds the shortest path in a non-weighted graph:
#-make a list to add all edges . -create a queue . -create a visited list to keep track of visits
# -when searching, if node is visited disregard, if not, add to queue
# -move queue to result list until queue empty . -give result/path that gets to all nodes
