n, k = map(int, input().split())
scores = list(map(int, input().split()))

# 점수를 내림차순으로 정렬
scores.sort(reverse=True)

# 상을 받는 커트라인 구하기
cutoff = scores[k-1]

print(cutoff)
