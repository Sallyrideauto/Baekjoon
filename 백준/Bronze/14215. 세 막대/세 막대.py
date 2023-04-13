def main():
    a, b, c = map(int, input().split())

    # 삼각형의 성립 조건: 가장 긴 변의 길이가 다른 두 변의 길이의 합보다 작아야 함
    sides = [a, b, c]
    sides.sort()

    if sides[0] + sides[1] > sides[2]:
        perimeter = sum(sides)
    else:
        perimeter = 2 * (sides[0] + sides[1]) - 1

    print(perimeter)

if __name__ == "__main__":
    main()

# 이 프로그램은 길이가 a, b, c인 세 막대를 가지고 만들 수 있는 가장 큰 둘레의 삼각형을 계산합니다.