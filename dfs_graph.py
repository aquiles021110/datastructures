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
graph={
    'a':['b','c'],
    'b':['a','d','e'],
    'c':['a','f'],
    'd':['b','e'],
    'e':['b'],
    'f':['c']
}
dfs(graph,'a')