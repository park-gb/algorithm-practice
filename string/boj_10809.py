# https://www.acmicpc.net/problem/10809

import string
alphabet = string.ascii_lowercase # abcdef...wxyz

input_string = input() # 단어 입력받기
answer = [-1]*len(alphabet) 

for idx in range(len(input_string)):
    # 알파벳이 한 번 이상 나왔을 경우
    if answer[alphabet.index(input_string[idx])] == -1:
        answer[alphabet.index(input_string[idx])] = idx

# 정답 출력
for ans in answer:
    print(ans, end = ' ')