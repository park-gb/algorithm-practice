# 문제 원본: https://www.acmicpc.net/problem/13458
# 개인해설: https://heytech.tistory.com/363
import sys; input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
Head, Sub = map(int, input().split())

answer = N
for i in range(N):
    arr[i] -= Head
    if arr[i] > 0:
        if arr[i]%Sub > 0:
            answer += arr[i]//Sub + 1
        else:
            answer += arr[i]//Sub
print(answer)