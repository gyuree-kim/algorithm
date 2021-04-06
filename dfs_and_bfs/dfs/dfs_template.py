graph = []
graph.append(list(map(int, input())))

# 1차원 그래프 
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 2차원 그래프
def dfs(x,y):
    # out of the map size
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    # haven't visited
    if graph[x][y] == 0 :
        graph[x][y] = 1 #check visited
        # reculsive calls for up, down, left, and right
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False