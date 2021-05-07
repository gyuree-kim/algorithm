# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    cnt = 0
    d.sort()
    for i in d:
        budget -= i
        if budget < 0 :
            break
        else :
            cnt += 1
    return cnt