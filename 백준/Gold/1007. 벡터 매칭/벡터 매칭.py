import itertools
import math

def vector_matching(points):
    N = len(points)
    total_x, total_y = 0, 0

    # 전체 점들의 합을 구합니다.
    for x, y in points:
        total_x += x
        total_y += y

    # 가능한 모든 조합을 탐색합니다.
    min_value = float('inf')
    for comb in itertools.combinations(points, N // 2):
        sum_x, sum_y = 0, 0
        # 선택된 조합의 합을 구합니다.
        for x, y in comb:
            sum_x += x
            sum_y += y

        # 선택되지 않은 점들의 벡터 합은 전체 벡터 합에서 조합의 벡터 합을 빼서 구합니다.
        diff_x = total_x - 2 * sum_x
        diff_y = total_y - 2 * sum_y
        min_value = min(min_value, math.sqrt(diff_x ** 2 + diff_y ** 2))

    return min_value

# 입력 예제
T = int(input())
for _ in range(T):
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    result = vector_matching(points)
    print(f"{result:.6f}")
