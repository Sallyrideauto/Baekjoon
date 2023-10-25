'''
각 도로를 직선으로 생각하면, 직선과 직선 사이의 거리는 다음 세 가지 경우 중 하나
1. 두 직선이 평행할 경우: 이 경우 두 직선 중 하나의 점에서 다른 직선까지의 수직 거리가 두 직선 사이의 거리입니다.
2. 두 직선이 교차할 경우: 이 경우 교차 지점이 있으므로 거리는 0입니다.
3. 두 직선이 교차하지 않고 평행하지 않은 경우: 이 경우 두 직선 사이의 거리는 두 직선에 속한 두 점 사이의 거리 중 최소값입니다.

로직:
1. 신촌에 연결된 모든 도로와 안암에 연결된 모든 도로 간의 거리를 계산합니다.
2. 두 도로 간의 최단 거리를 찾습니다.
'''

import sys


def dot(A, B, E):
    return (B[0] - A[0]) * (E[0] - A[0]) + (B[1] - A[1]) * (E[1] - A[1])

def dist_line(A, B, E):
    AB = [B[0] - A[0], B[1] - A[1]]
    BE = [E[0] - B[0], E[1] - B[1]]
    AE = [E[0] - A[0], E[1] - A[1]]

    if dot(A, B, E) < 0: return (AE[0] ** 2 + AE[1] ** 2) ** 0.5
    if dot(B, A, E) < 0: return (BE[0] ** 2 + BE[1] ** 2) ** 0.5
    f = abs(AB[0] * AE[1] - AB[1] * AE[0])
    return f / ((AB[0] ** 2 + AB[1] ** 2) ** 0.5)


def dist_segment(A, B, E, F):
    if A == E or A == F: return 0
    if B == E or B == F: return 0
    return min(dist_line(A, B, E), dist_line(A, B, F), dist_line(E, F, A), dist_line(E, F, B))


n, m = map(int, input().split())

shinchon = [list(map(float, input().split())) for _ in range(n)]
anam = [list(map(float, input().split())) for _ in range(m)]

answer = float('inf')
for i in range(n):
    for j in range(m):
        answer = min(answer, dist_segment(shinchon[i][:2], shinchon[i][2:], anam[j][:2], anam[j][2:]))

print(answer)
