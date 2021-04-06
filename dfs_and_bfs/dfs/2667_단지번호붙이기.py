# 문제: git commit -m "[DFSBFS] Upload 2178, 2606, 2667
# 코드: http://colorscripter.com/s/KY5AY83

from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

num = 0
def dfs(x,y):
    global num 
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    # 방문하지 않았을 경우  
    if graph[x][y] == 1 :
        graph[x][y] = 0 # 방문 체크
        num += 1        # 집의 수 
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

count = 0   # 단지 수
houses = [] # 집의 수 리스트 
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True: 
            houses.append(num)
            count += 1
            num = 0
print(count)

houses.sort()
for house in houses: print(house)