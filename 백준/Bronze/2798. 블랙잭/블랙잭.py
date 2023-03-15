n, m = map(int, input().split())
cards = list(map(int, input().split()))
max_sum = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum_cards = cards[i] + cards[j] + cards[k]
            if sum_cards <= m and sum_cards > max_sum:
                max_sum = sum_cards
                
print(max_sum)
