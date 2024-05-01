# 도시의 개수 입력
n = int(input())

# 도로 길이 입력
distances = list(map(int, input().split()))

# 주유소 가격 입력
prices = list(map(int, input().split()))

# 총 비용 계산
total_cost = 0
# 현재까지의 주유소 가격 중 가장 저렴한 가격
min_price = prices[0]

# 각 도로 구간에 대한 비용 계산
for i in range(n - 1):
    # 더 저렴한 가격을 찾으면 업데이트
    if prices[i] < min_price:
        min_price = prices[i]

    # 도로 구간의 비용을 계산하여 누적
    total_cost += min_price * distances[i]

print(total_cost)    