import math

def find_min_operations(x, y):
    distance = y - x
    sqrt_dist = int(math.sqrt(distance))

    if distance == sqrt_dist * sqrt_dist:
        return 2 * sqrt_dist - 1
    elif sqrt_dist * sqrt_dist < distance <= sqrt_dist * (sqrt_dist + 1):
        return 2 * sqrt_dist
    else:
        return 2 * sqrt_dist + 1

def main():
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split())
        print(find_min_operations(x, y))

if __name__ == "__main__":
    main()

"""
이 프로그램은 find_min_operations 함수를 사용하여 
x지점부터 y지점까지 이동하는데 필요한 최소한의 공간 이동 장치 작동 횟수를 구합니다. 
각 테스트 케이스에 대해 결과를 출력합니다.
"""