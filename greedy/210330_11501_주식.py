#baekjoon, 11501, 주식 

n = int(input())
values_list = []
benefit = 0

#input values
for i in range(n):
    days = int(input())
    values = list(map(int, input().split()))
    values_list.append(values)

# calcuate result
for values in values_list :
    benefit = 0
    max_val = values[-1]
    for value in values[::-1] :
        if max_val < value : max_val = value
        elif max_val > value : benefit += max_val - value
    print(benefit)