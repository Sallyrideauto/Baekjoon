'''
이 문제를 풀기 위해서는 주어진 연산 🍰에 따라 주어진 케이크 수 a와 c를 사용하여 케이크 수 b를 찾아야 합니다.
우리에게 주어진 연산 🍰는 다음과 같이 정의됩니다:

[ a 🍰 b = (a.z + b.x, a.y * b.y, a.x + b.z) ]

그리고 문제는 다음과 같이 a 🍰 b = c를 만족하는 b를 찾으라고 합니다.

이 식을 b에 대해 풀면 다음과 같습니다:
1. ( b.x = c.x - a.z )
2. ( b.y = c.y / a.y ) (주어진 조건에 의해 a.y와 c.y는 자연수이므로, c.y는 a.y의 배수입니다.)
3. ( b.z = c.z - a.x )
'''

def find_b(a, c):
    '''
    주어진 케이크 수 a와 c를 사용하여 연산 🍰에 따라 케이크 수 b를 찾는 함수

    :param a: 케이크 수 a를 구성하는 튜플(a.x, a.y, a.z)
    :param c: 케이크 수 c를 구성하는 튜플(c.x, c.y, c.z)
    :return: 케이크 수 b를 구성하는 튜플(b.x, b.y, b.z)
    '''

    b_x = c[0] - a[2]
    b_y = c[1] // a[1]  # // 연산자는 나눗셈 후 정수 부분만 반환
    b_z = c[2] - a[0]

    return (b_x, b_y, b_z)

a_x, a_y, a_z = map(int, input().split())
c_x, c_y, c_z = map(int, input().split())

# 케이크 수 a와 c
a = (a_x, a_y, a_z)
c = (c_x, c_y, c_z)

# 케이크 수 b 계산
b = find_b(a, c)

print(f"{b[0]} {b[1]} {b[2]}")