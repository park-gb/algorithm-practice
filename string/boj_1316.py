# https://www.acmicpc.net/problem/1316
import string
input_string = [input() for _ in range(int(input()))]

alphabet_dict = dict()
answer = 0
for word in input_string:
    word_len = len(word)
    if word_len < 3: # 문자열 길이가 2 이하인 경우는 그룹 단어
        answer+=1
        continue
    # 알파벳 출현여부 저장할 딕셔너리 생성
    for alphabet in string.ascii_lowercase:
        alphabet_dict[alphabet] = 0
    
    # 단어 내 좌측부터 한 글자씩 인덱싱
    for i in range(word_len):
        # 마지막 글자까지 인덱싱한 경우
        if i == word_len - 1:
            # 최초 등장한 알파벳이거나 동일한 알파벳이 연속해서 등장한 경우는 그룹 단어
            if alphabet_dict[word[i]] == 0 or word[i-1] == word[i]:
                answer+=1
                break
        elif alphabet_dict[word[i]] == 0: # 최초 등장한 알파벳인 경우
            alphabet_dict[word[i]] = 1 # 알파벳 등장 체크
            continue
        # 기존에 등장한 알파벳이지만 해당 알파벳과 그룹핑이 안되는 경우(직전 알파벳이 종류가 다른 경우)
        elif alphabet_dict[word[i]] == 1 and word[i-1] != word[i]:
            # 그룹 단어 아님
            break
print(answer)    