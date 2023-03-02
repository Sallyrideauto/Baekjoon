n, m = map(int, input().split())

# 바구니 번호를 저장한 리스트
baskets = [i for i in range(1, n+1)]

for i in range(m):
    # 역순으로 만들 범위를 입력받음
    start, end = map(int, input().split())
    # 범위 내의 바구니를 역순으로 뒤집음
    baskets[start-1:end] = reversed(baskets[start-1:end])

# 결과 출력
print(*baskets)
