import sys; input = sys.stdin.readline
from collections import deque

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 0))
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt > 10:
            return -1

        for dx, dy in d:
            nrx, nry, r_cnt = move(rx, ry, dx, dy)
            nbx, nby, b_cnt = move(bx, by, dx, dy)
            if board[nbx + dx][nby + dy] == 'O':
                continue
            if board[nrx + dx][nry + dy] == 'O' and cnt < 10:
                return (cnt + 1)
            if nrx == nbx and nry == nby:
                if r_cnt > b_cnt:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            if nrx == rx and nry == ry and nbx == bx and nby == by:
                continue
            q.append((nrx, nry, nbx, nby, cnt + 1))
    return -1

def move(x, y, dx, dy):
    nx = x
    ny = y
    move_cnt = 0
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