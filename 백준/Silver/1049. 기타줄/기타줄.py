def find_minimum_cost(n, m, prices):
    # 세트와 낱개의 최저 가격 초기화
    min_set_price = float('inf')
    min_individual_price = float('inf')
    
    # 모든 브랜드의 가격을 비교하여 최저 가격을 찾기
    for set_price, individual_price in prices:
        if set_price < min_set_price:
            min_set_price = set_price
        if individual_price < min_individual_price:
            min_individual_price = individual_price
            
    # 1. 세트로만 사는 경우
    total_set_only_cost = (n // 6) * min_set_price + (min_set_price if n % 6 != 0 else 0)
    
    # 2. 세트와 낱개를 조합해서 사는 경우
    total_mixed_cost = (n // 6) * min_set_price + (n % 6) * min_individual_price
    
    # 3. 낱개로만 사는 경우
    total_individual_only_cost = n * min_individual_price
    
    # 세 가지 방법 중 가장 저렴한 가격 선택
    return min(total_set_only_cost, total_mixed_cost, total_individual_only_cost)
    
n, m = map(int, input().split())
prices = [tuple(map(int, input().split())) for _ in range(m)]

# 최소 비용 계산
min_cost = find_minimum_cost(n, m, prices)

print(min_cost)