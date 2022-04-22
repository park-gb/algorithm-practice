import sys; input = sys.stdin.readline
from itertools import combinations

def solve():
    global answer
    # start 팀을 구성할 수 있는 모든 경우
    for start_member in list(combinations(member_all, N//2)):
        start_total = link_total = 0
        # link 팀원 = 전체 멤버에서 start 팀원 제외
        link_member = list(set(member_all) - set(start_member))
        # 팀별 능력치 시너지(S_ij + S_ji) 계산
        for i, j in list(combinations(start_member, 2)):
            start_total += s_all[i][j]
            start_total += s_all[j][i]
        for i, j in list(combinations(link_member, 2)):
            link_total += s_all[i][j]
            link_total += s_all[j][i]
        answer = min(answer, abs(start_total - link_total))

if __name__ == "__main__":
    N = int(input())
    s_all = [list(map(int, input().split())) for _ in range(N)]
    # 전체 팀원 번호
    member_all = list(range(N))
    answer = int(1e9)
    solve()
    print(answer)