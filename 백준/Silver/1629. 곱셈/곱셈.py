def power_mod(a, b, c):
    if b == 1:
        return a % c
    temp = power_mod(a, b // 2, c)
    if b % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * a % c

a, b, c = map(int, input().split())
result = power_mod(a, b, c)
print(result)

"""
이 프로그램은 자연수 A, B, C를 입력받아 A를 B번 곱한 수를 C로 나눈 나머지를 출력합니다. 
분할 정복 방식을 사용하여 거듭제곱의 시간 복잡도를 줄였습니다.
"""