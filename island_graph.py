from collections import deque
def dfs(graph,node,visited=None):
    if visited==None:
        visited=set()
        #when we start with a node it is marked as visited
    visited.add(node)
    print(node,end='-')
    #deep dive into  neighbour nodes of unvisited nodes
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
def count_components(graph):
    visited=set()
    count=0   
    for node in graph:
        if node not in visited:
            count+=1
            dfs(graph, node, visited)
    return count

graph={
    'a':['b'],
    'b':[],
    'c':['d'],
    'd':[]
}
#complete
print(count_components(graph))
