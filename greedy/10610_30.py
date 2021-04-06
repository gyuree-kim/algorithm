# n = input()

# if (int(n))%30 == 0 :
#     print(int(n))

# if '0' in n :
#     s = sum([int(i) for i in n])
#     n = list(n)
#     if s%3 == 0 :
#         n.sort(reverse=True)
#         idx = n.index('0')
#         temp = n[-1]
#         n[idx] = temp
#         n[-1] = '0'
#         for i in n : print(i, end="")
# else : 
#     print(-1)  

# n = input()
# n = list(n)
# n.sort(reverse = True)
# s = sum([int(i) for i in n])
# if s % 3 == 0 :
#     for i in n : print(i, end="")
# else : print(-1)

# 더 나은 풀이
n = input()
n = list(n)
n.sort(reverse = True)
n = int(''.join(n))
if n % 30 == 0 :
    print(n)
else : print(-1)