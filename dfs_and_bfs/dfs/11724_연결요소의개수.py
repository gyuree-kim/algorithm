# 문제: https://www.acmicpc.net/problem/11724
# 코드: http://colorscripter.com/s/FZA7N9I
from collections import deque
import sys
sys.setrecursionlimit(10000)

# 입력 값
n, m = map(int,sys.stdin.readline().split()) #정점과 간선의 개수 
graph = [[] for _ in range(n+1) ]  #1부터 시작
visited = [False]*(n+1)  #1부터 시작 
visited[0] = True
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# 연결요소 개수(connected component) 계산
count = 0
for v in visited:
    if not v:
        dfs(visited.index(v))
        count += 1
print(count)
