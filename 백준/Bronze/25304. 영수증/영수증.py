X = int(input())
N = int(input())

receipt = []

for i in range(N):
    a, b = map(int, input().split())
    costs = a * b
    receipt.append(costs)

sum_receipt = sum(receipt)

if sum_receipt == X:
    print("Yes")
else:
    print("No")