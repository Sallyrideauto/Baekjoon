# 최대공약수를 구하는 함수 gcd를 사용

from math import gcd
from functools import reduce

def main():
    # 입력 받기
    n = int(input())
    trees = [int(input()) for _ in range(n)]

    # 가로수 사이의 거리 구하기
    distances = [trees[i+1] - trees[i] for i in range(n-1)]

    # 거리들의 최대공약수 구하기
    gcd_of_distances = reduce(gcd, distances)

    # 추가로 심어야 할 가로수의 수 계산
    additional_trees = sum([(dist // gcd_of_distances) - 1 for dist in distances])

    print(additional_trees)

if __name__ == "__main__":
    main()

"""
이 프로그램은 이미 심어져 있는 가로수의 위치를 입력 받아 최대공약수를 구하고, 
그 간격으로 가로수를 채울 수 있는지 확인한 다음, 
추가로 심어야 할 가로수의 최소 개수를 출력합니다.
"""