button_a = 300 # 5분 = 5 * 60초
button_b = 60  # 1분 = 60초
button_c = 10  # 10초

T = int(input())  # 요리시간 T를 입력받음

count_a = count_b = count_c = 0  # 각 버튼의 누른 횟수를 저장할 변수 초기화

while T > 0:
    if T >= button_a:
        T -= button_a
        count_a += 1
    elif T >= button_b:
        T -= button_b
        count_b += 1
    elif T >= button_c:
        T -= button_c
        count_c += 1
    else:
        break

if T != 0:  # 요리시간 T를 맞출 수 없는 경우
    print("-1")
else:  # 요리시간 T를 맞출 수 있는 경우
    print(count_a, count_b, count_c)
