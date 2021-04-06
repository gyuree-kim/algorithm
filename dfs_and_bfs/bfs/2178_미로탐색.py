# 문제링크: https://www.acmicpc.net/problem/2178
# 코드링크: http://colorscripter.com/s/GhIHpBO
from collections import deque

# Input values
n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# bfs algorithm
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    # Availabel directions: up, down, left, right
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # when if it is out of the map size
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # when if it meets wall
            if graph[nx][ny] == 0 :
                continue
            # update graph with shortest length
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    # return shortest length
    return graph[n-1][m-1]

# print result
print(bfs(0,0))