#Breadth First Search
from collections import deque
def bfs(graph,start_node):
    visited=set()
    queue=deque([start_node])
    visited.add(start_node)
    while queue:
        node=queue.popleft()
        print(node,end='-')
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
graph={
    'a':['b','c'],
    'b':['a','d','e'],
    'c':['a','f'],
    'd':['b','e'],
    'e':['b'],
    'f':['c']
}
bfs(graph,'a')