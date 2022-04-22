import sys; input = sys.stdin.readline

def solve(i, res):
    global ans_max, ans_min
    global add, sub, mul, div
    if i == N:
        ans_max = max(ans_max, res)
        ans_min = min(ans_min, res)
        return
    else:
        if add:
            add -= 1
            solve(i + 1, res + num_list[i])
            add += 1
        if sub:
            sub -= 1
            solve(i+ 1, res - num_list[i])
            sub += 1
        if mul:
            mul -= 1
            solve(i+ 1, res * num_list[i])
            mul += 1
        if div:
            div -= 1
            solve(i + 1, int(res / num_list[i]))
            div += 1

if __name__ == "__main__":
    N = int(input())
    num_list = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    ans_min = int(1e10)
    ans_max = -int(1e10)
    solve(1, num_list[0])
    print(ans_max)
    print(ans_min)