X = int(input())

# 몇 번째 대각선 위에 있는지 구하기
i = 1
while X > i:
    X -= i
    i += 1

# 대각선에서 몇 번째에 위치하는지 구하기
if i % 2 == 0:
    # 대각선이 짝수번째면 분자는 작아지고 분모는 커집니다.
    numerator = X
    denominator = i - X + 1
else:
    # 대각선이 홀수번째면 분자는 커지고 분모는 작아집니다.
    numerator = i - X + 1
    denominator = X

print("{}/{}".format(numerator, denominator))
