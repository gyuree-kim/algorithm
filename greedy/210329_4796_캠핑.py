#https://www.acmicpc.net/problem/4796

arr = []

while True:
    data = list(map(int, input().split()))
    if data == [0,0,0] :
        break
    else :
        arr.append(data)
        
for i,(L,P,V) in enumerate(arr):
    count = (V//P)*L
    if V%P >= L :
        count += L
    else :
        count += V % P
    print(f"Case {i+1}: {count}")