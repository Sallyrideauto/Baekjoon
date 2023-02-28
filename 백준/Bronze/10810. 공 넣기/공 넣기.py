def put_balls(baskets, start, end, ball):
    for i in range(start-1, end):
        baskets[i] = ball

def print_balls(baskets):
    for basket in baskets:
        print(basket, end=' ')

n, m = map(int, input().split())
baskets = [0] * n

for _ in range(m):
    start, end, ball = map(int, input().split())
    put_balls(baskets, start, end, ball)

print_balls(baskets)
