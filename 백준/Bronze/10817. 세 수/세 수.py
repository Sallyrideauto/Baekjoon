rank = []
A, B, C = map(int, input().split())

rank.append(A)
rank.append(B)
rank.append(C)

rank.sort()

print(rank[1])