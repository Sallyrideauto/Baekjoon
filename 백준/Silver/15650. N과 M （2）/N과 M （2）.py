from itertools import combinations

N, M = map(int, input().split())

# 1부터 N까지의 수 중에서 M개를 선택하는 경우의 수를 구함
cases = combinations(range(1, N+1), M)

# 조건을 만족하는 수열을 출력
for case in cases:
    print(*case)

"""
위 프로그램은 itertools 모듈의 combinations 함수를 이용하여 
1부터 N까지의 수 중에서 M개를 고르는 모든 경우의 수를 구한 뒤, 
그 중에서 오름차순인 경우만 출력하는 것입니다. 
combinations 함수는 (range(1, N+1), M)를 인자로 받아 
1부터 N까지의 수 중에서 M개를 선택하는 경우의 수를 구합니다. 
그리고 for문으로 모든 경우에 대해서 출력하면 됩니다. 
출력할 때, *case를 사용하여 튜플 형태로 출력되는 것을 공백으로 구분된 형태로 출력합니다.
"""