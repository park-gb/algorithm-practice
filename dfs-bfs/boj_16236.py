import sys; input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    global shark_size
    visited = [[False]*N for _ in range(N)]
    shark = []
    q = deque()
    q.append((0, x, y))
    while q:
        dist, x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]
                visited[nx][ny] = True
                if 1 <= graph[nx][ny] <= 6 and graph[nx][ny] < shark_size:
                    q.append((dist + 1, nx, ny))
                    shark.append((dist + 1, nx, ny))
                elif graph[nx][ny] == 0 or shark_size == graph[nx][ny]:
                    q.append((dist+1, nx, ny))

    if shark:
        return sorted(shark)[0]
    else:
        return False

def solve(x, y):
    global answer
    global shark_size
    eat = 0
    while True:
        shark = bfs(x, y)
        if shark:
            dist, x_shark, y_shark = shark
            graph[x_shark][y_shark] = 0
            eat += 1
            answer += dist
            if eat == shark_size:
                shark_size += 1
                eat = 0
            x = x_shark
            y = y_shark
        else:
            break

def exist_fish():
    for i in range(N):
        for j in range(N):
            if 1 <= graph[i][j] <= 6:
                return True
    return False

def find_shark():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                x_shark = i
                y_shark = j
    return x_shark, y_shark

if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    shark_size = 2
    if not exist_fish():
        print(0)
        exit(0)
    else:
        d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        x, y = find_shark()
        graph[x][y] = 0

        answer = 0
        solve(x, y)
        print(answer)