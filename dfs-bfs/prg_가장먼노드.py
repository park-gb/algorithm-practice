# https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3
from collections import deque
def solution(n, edge):
    answer = 0
    dist = [0]*(n+1)
    edge.sort()
    q = deque()
    graph = [[] for i in range(n+1)]
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    q.append(1)
    dist[1] = 1
    
    while q:
        start = q.popleft()
        for end in graph[start]:
            if dist[end]==0:
                q.append(end)
                dist[end] = dist[start] + 1
        
    dist_max = max(dist)
    for d in dist:
        if d == dist_max:
            answer+=1     
    return answer