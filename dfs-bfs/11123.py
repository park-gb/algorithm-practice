from collections import deque

# 테스트 케이스 개수 입력받기 
test_num = int(input())

# (y, x) 탐색 방향 설정(상, 하, 좌, 우)
d = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(y, x):
    # 새롭게 발견한 양의 위치를 저장할 큐 생성
    q = deque()
    q.append((y, x))
    # 발견한 양의 중복 탐지 방지
    graph[y][x] = '.'
    # 양들의 무리 수 확인이 끝날 때까지 반복 수행
    while q:
        y, x = q.popleft()
        # 상, 하, 좌, 우 인접한 양 찾기
        for dy, dx in d:
            y_new, x_new = y + dy, x + dx
            # 그래프 범위 내 미탐색 양 발견 시
            if (0 <= y_new < h) and (0 <= x_new < w) and graph[y_new][x_new] == '#':
                # 새롭게 발견한 양은 큐에 삽입
                q.append((y_new, x_new))
                # 발견한 양의 중복 탐지 방지
                graph[y_new][x_new] = '.'

# 테스트 케이스마다 결괏값(양 무리 수) 출력
for _ in range(test_num):
    # 양들의 위치 정보 입력받기
    h, w = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    # 결괏값: 양 무리 수 
    answer = 0
    for i in range(h):
        for j in range(w):
            # 양이 발견된 지점부터 탐색 시작
            if graph[i][j] == '#':
                bfs(i, j)
                answer += 1
    print(answer)