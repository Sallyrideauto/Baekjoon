import math

n = int(input()) # 시험장의 개수
a = list(map(int, input().split())) # 각 시험장의 응시자 수
b, c = map(int, input().split()) # 총감독관, 부감독관이 감시할 수 있는 응시자 수

# 총감독관이 감시할 수 있는 응시자 수보다 적은 경우에는 1명으로 충분하다.
# 그렇지 않은 경우에는, 감독관이 1명 필요하므로 총 감독관을 1명 더해주고, 총 감독관이 감시한 후에 남은 응시자 수에 대해서 부감독관이 감시할 수 있는 응시자 수를 나누어 올림한 값을 더해준다.
answer = 0
for i in range(n):
    answer += 1
    a[i] -= b
    if a[i] > 0:
        answer += math.ceil(a[i] / c)
print(answer)
