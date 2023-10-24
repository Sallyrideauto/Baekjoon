def hanoi(n, start, end, via):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, via, end)    # 첫 번쨰 단계 : n - 1개의 원판을 첫 번째 장대에서 두 번째 장대로 이동
    print(start, end)    # 두 번째 단계 : n번째 원판을 첫 번째 장대에서 세 번째 장대로 이동
    hanoi(n - 1, via, end, start)    # 세 번째 단계 : n - 1개의 원판을 두 번째 장대에서 세 번째 장대로 이동
    
N = int(input())
print(2 ** N - 1)    # 전체 이동 횟수는 2의 N 제곱에서 1을 뺀 값
hanoi(N, 1, 3, 2)    # 원판의 개수 N, 시작 장대 1, 목적 장대 3, 경유 장대 2를 파라미터로 전달