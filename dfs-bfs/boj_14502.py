# 문제 원본: https://www.acmicpc.net/problem/14502
# 개인 해설: https://heytech.tistory.com/368
import sys; input = sys.stdin.readline
import copy

# 벽 건설 함수
def wall_construct(wall_cnt):
    # 벽 3개 설치 완료 시, 바이러스 전파
    if wall_cnt == 3:
        virus_spread()
        return
    # 벽을 설치할 수 있는 모든 경우의 수 확인
    for n in range(N):
        for m in range(M):
            if board[n][m] == 0:
                board[n][m] = 1 # 벽 설치
                wall_construct(wall_cnt + 1)
                board[n][m] = 0 # 새로운 조합 만들기 위해 초기화

# 바이러스 전파 함수
def virus_spread():
    global answer
    # 기존 맵 정보 깊은 복사(Deep Copy)
    board_wall = copy.deepcopy(board)
    # 바이러스 위치
    virus = [(n, m) for n in range(N) for m in range(M) if board_wall[n][m] == 2]

    # 바이러스마다 전파 끝날 때까지 반복
    while virus:
        x, y = virus.pop()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and board_wall[nx][ny] == 0:
                board_wall[nx][ny] = 2
                virus.append((nx, ny)) # 바이러스 전파

    # 안전지대 개수 카운팅
    safezone_cnt = 0
    for row in board_wall:
        safezone_cnt += row.count(0)
    answer = max(answer, safezone_cnt)

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = 0
    wall_construct(0)
    print(answer)
