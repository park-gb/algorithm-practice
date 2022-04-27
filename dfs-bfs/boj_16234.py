import sys; input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    union_contry = []
    union_contry.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union_contry.append((nx, ny))
    return union_contry

if __name__ == '__main__':
    N, L, R = map(int, input().split())
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    graph = [[0]*N for _ in range(N)]

    for i in range(N):
        data = list(map(int, input().split()))
        for j in range(N):
            graph[i][j] = data[j]

    answer = 0
    while True:
        visited = [[False]*N for _ in range(N)]
        move = False
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    visited[i][j] = True
                    union_contry = bfs(i, j)
                    if 1 < len(union_contry):
                        move = True
                        population = sum([graph[x][y] for x, y in union_contry]) // len(union_contry)
                        for x, y in union_contry:
                            graph[x][y] = population

        # 모든 나라를 탐색했지만 인구 이동이 일어나지 않은 경우 무한 루프 탈출
        if not move:
            break
        # 인구 이동이 일어났기 때문에 1일 추가
        else:
            answer += 1
    print(answer)