# http://colorscripter.com/s/HS3D58U
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
              
from collections import deque
n,m,v = map(int, input().split())
visited = [False]*(n+1)
graph = [[] for _ in range(int(n)+1)]
for i in range(int(m)):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
for i in range(int(n+1)):
    graph[i].sort()
dfs(graph, v, visited)
print()
visited = [False]*(n+1)
bfs(graph, v, visited) 

