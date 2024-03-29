"""
점화식 정의
D[n] = 길이가 n인 이진수열의 개수
D[n] = D[n-1] + D[n-2] (n>=3)

입력으로 주어진 자연수 n을 입력 받아서, 
길이가 n인 이진수열의 개수를 15746으로 나눈 나머지를 출력합니다.
"""

n = int(input())
d = [0] * (n+1)
d[1] = 1
if n >= 2:
    d[2] = 2
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]) % 15746
print(d[n])
