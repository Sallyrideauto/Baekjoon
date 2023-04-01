N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for i in range(M):
    B.append(list(map(int, input().split())))

C = [[0] * K for i in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

for i in range(N):
    print(' '.join(map(str, C[i])))

"""
먼저 입력으로 받은 두 행렬 A와 B를 각각 이차원 리스트로 저장합니다. 
그리고 결과 행렬 C를 생성한 후, C의 각 원소를 계산하여 저장합니다. 
마지막으로 C를 출력합니다.
"""