def main():    
    n = int(input()) # 문자열 개수
    n_total = input() # 숫자 N개 문자열로 입력
    answer = 0
    for number in n_total:
        answer+= int(number)
    print(answer)
    
if __name__ == "__main__":
    main()