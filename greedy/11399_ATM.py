#baekjoon, 11399, ATM 

n = int(input())
P = list(map(int, input().split()))
P.sort()

sum = 0
for i in range(n):
    sum += (n-i)*P[i]
print(sum)