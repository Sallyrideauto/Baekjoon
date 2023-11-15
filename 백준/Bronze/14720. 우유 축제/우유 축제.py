N = int(input())
milk_shop = list(map(int, input().split()))

max_drink = 0
next_milk = 0  # 영학이가 마셔야 할 다음 우유의 종류

for milk in milk_shop:
    if milk == next_milk:
        max_drink += 1
        next_milk = (next_milk + 1) % 3 # 다음 우유 순서로 넘어감

print(max_drink)