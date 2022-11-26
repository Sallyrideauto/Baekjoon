N = int(input())

tax22p = (N * 22) // 100
cost = (N * 80) // 100
leftfee = (N * 20) // 100
left22p = (leftfee * 22) // 100

A = N - tax22p
B = N - left22p

print(A, B)