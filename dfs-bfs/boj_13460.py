import sys; input = sys.stdin.readline
from collections import deque

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 0))
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        for dx, dy in d:
            nrx, nry, r_cnt = move(rx, ry, dx, dy)
            nbx, nby, b_cnt = move(bx, by, dx, dy)
            # Blue 공이 먼저 구멍에 들어갈 시, 다른 방향으로 이동
            if board[nbx + dx][nby + dy] == 'O':
                continue
            # Red 공이 구멍에 들어갈 시, 움직인 횟수 1 증가하고 종료(단, 10회 미만인 경우)
            if board[nrx + dx][nry + dy] == 'O' and cnt < 10:
                return cnt + 1
            # Red 공과 Blue 공이 만날 시, 먼저 도착한 공이 자리 차지
            if nrx == nbx and nry == nby:
                # Red 공이 먼저 도착 시, Blue 공을 한 칸 뒤로 이동
                if r_cnt < b_cnt:
                    nbx -= dx
                    nby -= dy
                else:
                    nrx -= dx
                    nry -= dy
            # 어떤 공도 움직이지 않는 경우
            if nrx == rx and nry == ry and nbx == bx and nby == by:
                continue

            if cnt < 10:
                q.append((nrx, nry, nbx, nby, cnt + 1))
            else:
                return -1
    return -1

def move(x, y, dx, dy):
    nx = x
    ny = y
    move_cnt = 0
    # 한 방향으로 이동할 수 있을 때까지 이동시키기
    while True:
        if board[nx+dx][ny+dy] != '#' and board[nx+dx][ny+dy] != 'O':
            nx += dx
            ny += dy
            move_cnt += 1
        else:
            break
    return nx, ny, move_cnt

if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    rx = ry = bx = by = ""
    for i in range(N):
        for j in range(M):
            if rx and ry and bx and by:
                break
            if board[i][j] == 'R':
                rx, ry = i, j
                continue
            if board[i][j] == 'B':
                bx, by = i, j
                continue

    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = bfs(rx, ry, bx, by)
    print(answer)