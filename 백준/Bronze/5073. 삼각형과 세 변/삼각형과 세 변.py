while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if a + b <= c or b + c <= a or c + a <= b:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")

"""
while True문은 무한 루프를 만듭니다.
a, b, c = map(int, input().split())은 세 개의 정수를 입력받아 a, b, c 변수에 할당합니다.
if a == b == c == 0: break는 입력이 0 0 0인 경우 루프를 종료합니다.
if a + b <= c or b + c <= a or c + a <= b: print("Invalid")는 주어진 세 변의 길이가 삼각형의 조건을 만족하지 않는 경우 "Invalid"를 출력합니다.
elif a == b == c: print("Equilateral")는 세 변의 길이가 모두 같은 경우 "Equilateral"를 출력합니다.
elif a == b or b == c or c == a: print("Isosceles")는 두 변의 길이만 같은 경우 "Isosceles"를 출력합니다.
else: print("Scalene")는 세 변의 길이가 모두 다른 경우 "Scalene"를 출력합니다.
"""