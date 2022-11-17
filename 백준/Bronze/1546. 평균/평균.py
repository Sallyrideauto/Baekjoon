N = int(input())
scores = [int(N) for N in input().split()]
M = int(max(scores))

result = []

for i in scores:
    score = (i / M) * 100
    result.append(score)

print(sum(result) / N)