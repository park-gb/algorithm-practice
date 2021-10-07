#https://www.acmicpc.net/problem/11399
n = int(input())
p_time = list(map(int, input().split()))
p_time.sort(reverse=True)
answer = 0
for i in range(1, n+1):
    answer += i*p_time[i-1]
print(answer)