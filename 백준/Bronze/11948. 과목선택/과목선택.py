sci_score = []
social_score = []

for _ in range(4):
    A = int(input())
    sci_score.append(A)

for _ in range(2):
    B = int(input())
    social_score.append(B)

sci_score.sort(reverse = True)
sci_score = sci_score[:3]
max_social_score = max(social_score)

print(sum(sci_score) + max_social_score)