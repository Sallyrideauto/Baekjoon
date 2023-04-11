def calculate_min_wins(x, y):
    total_score = x + y
    if total_score == 0:
        return 0

    # 이진 탐색을 사용하여 가능한 턴의 개수를 찾습니다.
    left, right = 1, int(2 * (10**12)**0.5) + 1
    while left <= right:
        mid = (left + right) // 2
        if mid * (mid + 1) // 2 == total_score:
            break
        elif mid * (mid + 1) // 2 < total_score:
            left = mid + 1
        else:
            right = mid - 1

    if mid * (mid + 1) // 2 != total_score:
        return -1

    # 윤호가 최소 몇 번 이겨야 하는지 계산합니다.
    min_wins = 0
    while x > 0:
        if x >= mid:
            x -= mid
            min_wins += 1
        mid -= 1

    return min_wins

def main():
    x, y = map(int, input().split())
    min_wins = calculate_min_wins(x, y)
    print(min_wins)

if __name__ == "__main__":
    main()

"""
이 프로그램은 윤호와 동혁이가 각각 x점과 y점을 얻을 수 있는지 확인하고, 
가능한 경우 윤호가 최소 몇 번 이겨야 하는지 계산하는 calculate_min_wins 함수를 사용합니다. 
입력 받은 점수에 대해 가능한 경우와 불가능한 경우에 따라 최소 승리 횟수 또는 -1을 출력합니다.
"""