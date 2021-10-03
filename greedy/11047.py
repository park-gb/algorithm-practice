# n: 화폐 종류 개수, k: 거스름돈
n, k = map(int, input().split())

# 화폐 종류 저장용 리스트 생성
money_list = []
for _ in range(n):
    # 화폐 종류 입력받기
    money_list.append(int(input()))

# 정답: 거스름용 화폐 개수의 최솟값
answer = 0

# 화폐 종류 내림차순 정렬: 화폐 가치가 큰 순서대로 화폐 정보 추출
money_list.sort(reverse = True)
for money in money_list:
    # 필요한 화폐 개수 = 거스름돈을 특정 화폐로 나눈 몫
    answer+= k//money
    # 거스름돈 업데이트: 거스름돈을 특정 화폐로 나눈 나머지로 업데이트
    k%=money
    # 거스름돈이 0원인 경우
    if k == 0:
        break
# 정답 출력
print(answer)