# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []

    for i in range(len(words)-1):
        if ( words[i][len(words[i])-1] != words[i+1][0] ) or (words[i+1] in words[:i+1]) :
            return [ (i+1)%n + 1, (i+1)//n + 1 ]
    return [0,0]