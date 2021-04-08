# 문제: https://www.acmicpc.net/problem/1697
# 코드: https://colorscripter.com/s/NId3qDE

from collections import deque
import sys
sys.setrecursionlimit(10**9)

n,k = map(int, sys.stdin.readline().split())
N = 100001
visited = [False]*N

def bfs(start, end):
    count = 0
    queue = deque([[start, count]])
    while queue:
        v,count = queue.popleft()
        
        # 방문하지 않았을 경우
        if not visited[v]:
            visited[v] = True
            # 종료 지점일 경우 리턴
            if v == end:
                break
            # 이동 횟수 계산
            count += 1
            if v*2 < N:
                queue.append([v*2, count])
            if v+1 < N:
                queue.append([v+1, count])
            if v-1 >= 0:
                queue.append([v-1, count])
    return count

print(bfs(n,k))

# while n == k:
#     if abs(n*2 - k) > (n-k):
#         n = n*2
#         count += 1
#     else :
#         count += (n-k)
# print(count)