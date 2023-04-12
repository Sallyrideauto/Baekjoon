def count_points(n):
    return (2 ** n + 1) ** 2

def main():
    n = int(input())
    result = count_points(n)
    print(result)

if __name__ == "__main__":
    main()

"""
이 프로그램은 중앙 이동 알고리즘을 사용하여 외계 지형을 만드는 과정을 N번 거친 후 점의 수를 계산하는 count_points 함수를 사용합니다. 
함수는 결과 값을 반환하며, 프로그램은 이 값을 출력합니다.
"""