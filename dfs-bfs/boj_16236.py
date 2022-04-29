# 문제 원본: https://www.acmicpc.net/problem/16236
# 개인 해설: https://heytech.tistory.com/375
import sys; input = sys.stdin.readline
from collections import deque

# 잡아먹을 수 있는 물고기 탐색 함수
def bfs(x, y):
    global shark_size
    visited = [[False]*N for _ in range(N)]
    fish = [] # 물고기 잡아먹을 시 소요거리 및 좌표정보 저장용 리스트
    q = deque()
    q.append((0, x, y))
    while q:
        dist, x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                # 잡아먹을 수 있는 물고기 존재하는 경우
                if 1 <= graph[nx][ny] <= 6 and graph[nx][ny] < shark_size:
                    q.append((dist + 1, nx, ny))
                    fish.append((dist + 1, nx, ny)) # 물고기 잡아먹을 때만 정보 저장
                # 빈 공간이거나 상어와 같은 크기의 물고기가 존재하는 경우
                elif graph[nx][ny] == 0 or shark_size == graph[nx][ny]:
                    q.append((dist+1, nx, ny))

    if fish:
        # 같은 거리에 여러마리의 물고기가 있을 경우를 대비하기 위해 리스트 정렬
        # '거리-행-열' 순으로 각각의 값이 작을수록 잡아먹는 데 우선순위가 높은 물고기
        return sorted(fish)[0]
    else:
        return False

# 최종정답 연산 함수
def solve(x, y):
    global answer
    global shark_size
    eat = 0
    # 잡아먹을 수 있는 물고기를 모두 잡아먹을 때까지 무한반복
    while True:
        fish = bfs(x, y)
        # 잡아먹은 물고기가 있는 경우
        if fish:
            dist, x_shark, y_shark = fish
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

# 물고기 존재여부 확인용 함수
def exist_fish():
    for i in range(N):
        for j in range(N):
            if 1 <= graph[i][j] <= 6:
                return True
    return False

# 상어 좌표 반환용 함수
def find_shark():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                return i, j

# 메인함수
if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    if not exist_fish():
        print(0)
        exit(0)
    else:
        shark_size = 2
        d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        x, y = find_shark()
        graph[x][y] = 0
        answer = 0
        solve(x, y)
        print(answer)