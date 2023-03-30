n = int(input())

count = 0
num = 666

while True:
    if '666' in str(num):
        count += 1
        if count == n:
            print(num)
            break
    num += 1

"""
먼저 입력값인 n을 정수로 받습니다. 
그리고 종말의 수가 몇 개 나왔는지 셀 변수 count와 현재 검사 중인 수를 저장하는 변수 num을 초기화합니다. 
while문을 사용하여 num부터 1씩 증가시키면서, num이 종말의 수인지 검사합니다. 
num을 문자열로 변환하여 '666'이 포함되어 있는지를 확인합니다. 
만약 포함되어 있다면 count를 증가시키고, count가 n과 같아졌을 때 num을 출력하고 while문을 종료합니다.
"""