T = int(input())

for i in range(1, T+1):        # 1부터 T까지
    A, B = map(int, input().split())
    print(f"Case #{i}: {A+B}")