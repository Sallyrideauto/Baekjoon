# https://ooyoung.tistory.com/46

input_num = int(input())
num = input_num # num 변수에 input_num을 지정

# 사이클 카운트 변수를 지정하고 while문 상단에서 sum_num과 new_num 구하기
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10)      # 각 자릿수를 더한 수
    new_num = ((num % 10) * 10) + (sum_num % 10)    # 새로 만들어지는 수
    cnt += 1    # 사이클 카운트
    # while문을 끝낼 조건식을 작성하고 끝나지 않을 경우 num의 값을 변경
    if new_num == input_num:
        break
    num = new_num   # num 변수에 last_num을 지정
print(cnt)