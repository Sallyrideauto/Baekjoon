def main():
    # 사용자 입력 받기
    min_val, max_val = map(int, input().split())

    # 제곱수의 배수를 체크할 배열, 초기값 False (배수 아님)
    is_square_multiple = [False] * (max_val - min_val + 1)

    # 제곱수 생성 및 배수 체크
    for i in range(2, int(max_val**0.5) + 1):
        square = i * i
        # 시작하는 배수 계산 (min_val 이상이면서 square의 배수)
        start = ((min_val + square - 1) // square) * square
        for j in range(start, max_val + 1, square):
            is_square_multiple[j - min_val] = True

    # 제곱수의 배수가 아닌 수의 개수 세기
    result = sum(1 for is_multiple in is_square_multiple if not is_multiple)
    print(result)

if __name__ == "__main__":
    main()
