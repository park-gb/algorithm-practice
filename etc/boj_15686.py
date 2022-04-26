# 문제 원본: https://www.acmicpc.net/problem/15686
# 개인 해설: https://heytech.tistory.com/374
import sys; input = sys.stdin.readline
from itertools import combinations

def solve():
    global answer
    for chicken in combinations(chicken_list, M):
        chicken_dist_total = 0
        for house in house_list:
            chicken_dist = int(1e9)
            for i in range(M):
                chicken_dist = min(chicken_dist, abs(house[0] - chicken[i][0]) + abs(house[1] - chicken[i][1]))
            chicken_dist_total += chicken_dist
        answer = min(answer, chicken_dist_total)
    return

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    house_list = []
    chicken_list = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                house_list.append((i, j))
            elif graph[i][j] == 2:
                chicken_list.append((i, j))
    answer = int(1e9)
    solve()
    print(answer)