import sys; input = sys.stdin.readline

def consult():
    for day in range(N-1, -1, -1):
        t = Work[day][0]  # 상담 소요일
        # 근무 가능한 경우
        if day + t <= N:
            p = Work[day][1]  # 상담 수입
            dp[day] = max(dp[day + 1], dp[day + t] + p)

        # 근무 불가능한 경우
        else:
            dp[day] = dp[day + 1]

if __name__ == "__main__":
    N = int(input())
    Work = [list(map(int, input().split())) for _ in range(N)]
    dp = [0]*(N+1)
    consult()
    answer = dp[0]
    print(answer)