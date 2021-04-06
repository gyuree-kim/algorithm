from collections import deque

n = int(input())
n,m = map(int, input().split())

# version1: linear
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

# version2: ^2
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