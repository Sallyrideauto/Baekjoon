def main():
    matrix = [list(map(int, input().split())) for _ in range(9)]
    max_value = -1
    max_row = -1
    max_col = -1

    for row in range(9):
        for col in range(9):
            if matrix[row][col] > max_value:
                max_value = matrix[row][col]
                max_row = row
                max_col = col

    print(max_value)
    print(max_row + 1, max_col + 1)

if __name__ == "__main__":
    main()

"""
이 프로그램은 9x9 격자판에 쓰여진 81개의 자연수 또는 0을 입력받아 
이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구합니다.
입력된 격자를 순회하며 최댓값과 그 위치를 업데이트해 나갑니다.
최종적으로 최댓값과 그 위치를 출력합니다.
"""