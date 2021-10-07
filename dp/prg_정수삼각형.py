'''
[문제]
https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3  

[풀이]
https://heytech.tistory.com/138
'''

def solution(triangle):
    while len(second) > 1:
        first = triangle.pop()
        second = triangle.pop()
        for i in range(len(second)):
            if first[i] < first[i+1]:
                second[i] += first[i+1]
            else:
                second[i] += first[i]
        triangle.append(second)
    return second[0]