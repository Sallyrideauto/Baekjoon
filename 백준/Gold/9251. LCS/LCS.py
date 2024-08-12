A = input()
B = input()

len_A, len_B = len(A), len(B)

dp = [
    [0 for _ in range(len_B + 1)]
    for _ in range(len_A + 1)
]

for i in range(1, len_A + 1):
    for j in range(1, len_B + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
lcs_length = dp[len_A][len_B]
print(lcs_length)