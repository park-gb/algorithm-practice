import sys; input = sys.stdin.readline

def rotate_clockwise(graph):
    temp = graph[7]
    for i in range(6, -1, -1):
        graph[i+1] = graph[i]
    graph[0] = temp

def rotate_countclockwise(graph):
    temp = graph[0]
    for i in range(7):
        graph[i] = graph[i + 1]
    graph[7] = temp

def dfs(i, rotate):
    global visited
    if not visited[i]:
        visited[i] = True
        left = graph[i][6]
        right = graph[i][2]
        if rotate == 1:
            rotate_clockwise(graph[i])
        else:
            rotate_countclockwise(graph[i])
        # 좌측에 톱니바퀴의 존재여부와 인접한 톱니 간 다른 극인지 확인
        if 1 <= i-1 and left != graph[i-1][2]:
            # 좌측 톱니바퀴를 현재 회전한 방향과 반대 방향으로 회전
            dfs(i - 1, -rotate)

        # 우측 톱니바퀴의 존재여부와 인접한 톱니 간 다른 극인지 확인
        elif i+1 <= 4 and right != graph[i+1][6]:
            # 우측 톱니바퀴를 현재 회전한 방향과 반대 방향으로 회전
            dfs(i + 1, -rotate)

def score():
    answer = 0
    for i in range(1, 5):
        if graph[i][0] == '1':
            answer += 2**(i-1)
    return answer

if __name__ == '__main__':
    graph = [[]]
    for _ in range(4):
        graph.append(list(input().rstrip()))
    K = int(input())

    for _ in range(K):
        i, rotate = map(int, input().split())
        visited = [False]*5
        dfs(i, rotate)

    answer = score()
    print(answer)