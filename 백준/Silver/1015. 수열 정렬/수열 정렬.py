def main():
    n = int(input())
    a = list(map(int, input().split()))

    sorted_indices = sorted(range(n), key=lambda x: a[x])
    p = [0] * n

    for i in range(n):
        p[sorted_indices[i]] = i

    print(*p)

if __name__ == "__main__":
    main()

# 이 프로그램은 배열 A의 크기 N과 배열 A의 원소를 입력 받아 비내림차순으로 만드는 수열 P를 출력합니다.