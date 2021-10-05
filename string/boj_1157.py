# https://www.acmicpc.net/problem/1157
from collections import Counter
input_string = input().lower() # 모든 문자 소문자로 치환
if len(input_string) == 1: # 문자열 길이가 1인 경우
    print(input_string.upper()) # 대문자로 출력
else: # 문자열 길이가 2 이상인 경우
    # 최다빈출 알파벳 2개 정보 선정
    char_cnt = Counter(input_string).most_common(2)
    # 출현 횟수가 공동 1위인 경우
    if char_cnt[0][1] == char_cnt[1][1]:
        print("?")
    # 출현 횟수가 단독 1위인 경우
    else:
        print(char_cnt[0][0].upper())