import sys
import heapq

# 보석, 가방 개수 입력
n, k = map(int, sys.stdin.readline().split())

# 보석 무게, 가격 입력
jwels = []
for _ in range(n):
    jwels.append(list(map(int, sys.stdin.readline().split())))
# 보석 무게별 오름차순
jwels.sort()

# 가방 최대 무게 입력
bags = []
for _ in range(k): 
    bags.append(int(sys.stdin.readline()))
# 가방 무게별 오름차순
bags.sort()

# 정답: 보석 가격 누적 합산용
answer = 0
# 힙 생성
jwels_heap = []
# 가방 하나씩 탐색
for bag in bags:
    # 탐색할 보석 존재 & 훔칠 수 있는 보석 존재
    while jwels and jwels[0][0] <= bag:
        # 보석 가격만 추출해 저장
        heapq.heappush(jwels_heap, -heapq.heappop(jwels)[1])
    
    # 훔칠 수 있는 보석이 있는 경우
    if jwels_heap:
        # 보석 가격 합산
        answer -= heapq.heappop(jwels_heap)
    
    # 모든 보석을 탐색했거나 가방에 넣을 수 있는 보석이 없는 경우
    elif not jwels:
        break

print(answer)