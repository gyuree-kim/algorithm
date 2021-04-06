# 문제: https://www.acmicpc.net/problem/2606
# 코드: http://colorscripter.com/s/PE6sxOx
from collections import deque
def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1) 

bfs(graph, 1, visited)
print(visited.count(True)-1) #1은 자기자신이므로 제외
