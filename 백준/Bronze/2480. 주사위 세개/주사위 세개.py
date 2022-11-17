A, B, C = map(int, input().split())
numbers = [A, B, C]

if A == B == C:
    print(10000 + A * 1000)
elif A == B != C or A == C:
    print(1000 + A * 100)
elif A != B == C:
    print(1000 + B * 100)
else:
    print(max(numbers) * 100)