N, X = map(int, input().split())

A = [int(N) for N in input().split()]
results = []

for i in A:
    if i < X:
        results.append(i)

print(*results)