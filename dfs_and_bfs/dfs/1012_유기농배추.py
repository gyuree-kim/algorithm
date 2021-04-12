# https://colorscripter.com/s/B7RqsQK

# -*- coding: utf-8 -*-
from collections import deque
import sys
sys.setrecursionlimit(10**9)
def dfs(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    # 방문하지 않았을 경우  
    if graph[x][y] == 1 :
        graph[x][y] = 2 # 방문 체크
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
T = int(input()) # 테스트케이스 개수
counts = [0]*T   # 각 테스트케이스의 배추흰지렁이 마리 수 
for i in range(T):
    # 배추 심은 위치 입력
    m,n,k = map(int, sys.stdin.readline().split()) #열, 행, 배추 위치 개수 
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    count = 0
    # dfs로 component 개수 계산 
    for row in range(n):
        for col in range(m):
            if dfs(row,col) == True: 
                count += 1  
    counts[i] = count  
# 결과 출력
for count in counts: print(count)



