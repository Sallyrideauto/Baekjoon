import math

B = int(input())

# 부가가치세를 제외한 가격 A 계산
A = math.ceil(B / 1.1)

print(A)