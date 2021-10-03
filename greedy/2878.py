# m: 사탕 개수, n: 친구 수
m, n = map(int, input().split())
# 친구별 사탕 수요 개수
candy_needs = [int(input()) for _ in range(n)]
# 사탕 수요 내림차순 정렬
candy_needs.sort(reverse = True)
# 정답: 친구들 분노 총합의 최솟값
answer = 0

for i in range(n):
    m-=candy_needs[i]

print(answer%(2**64))