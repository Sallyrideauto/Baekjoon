n, m = map(int, input().split())

# 바구니 초기화
basket = list(range(1, n+1))

# 공 교환
for i in range(m):
    a, b = map(int, input().split())
    basket[a-1], basket[b-1] = basket[b-1], basket[a-1]

# 결과 출력
print(' '.join(map(str, basket)))
