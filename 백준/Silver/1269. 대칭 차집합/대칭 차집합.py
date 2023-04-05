n, m = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

diff_a_b = len(set_a - set_b)
diff_b_a = len(set_b - set_a)

sym_diff = diff_a_b + diff_b_a

print(sym_diff)

"""
우선 입력으로 두 개의 집합 A와 B를 입력받고, 
set 자료형을 이용하여 중복을 제거하고 차집합 연산을 이용해 대칭 차집합을 계산합니다. 
차집합 연산을 이용해 구한 diff_a_b와 diff_b_a를 더한 값을 출력합니다.
"""