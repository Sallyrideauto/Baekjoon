'''
시간 초과가 발생한 것을 고려하면, 입력된 값 N이 매우 큰 경우에 해당 알고리즘의 수행 시간이 너무 길어지는 것으로 보입니다.

본 문제의 요구사항에 따르면 N은 최대 26이지만, 이때 필요한 연산 수는 2^26 - 1로, 이는 상당히 큰 숫자입니다.
따라서 직접적인 재귀 호출 방식으로 모든 연산을 출력하려면 많은 시간이 소요됩니다.

문제를 해결하기 위한 방법은 중심 공의 이동만을 직접 계산하고, 나머지 이동은 계산하지 않는 것입니다.
중심 공의 이동만 출력하면 되기 때문에, 이 방식을 사용하면 시간 복잡도를 크게 줄일 수 있습니다.

중심 공의 이동 패턴은 다음과 같습니다:
1. 처음 N개의 공 중에서 중심 공은 N // 2 + 1 번째 공입니다.
2. 이 중심 공은 다음과 같은 순서로 이동합니다: 1 -> 2, 1 -> 3, 2 -> 3.
'''

def move_center_ball(n, source, auxiliary, target):
    if n == 0:
        return
    mid = n // 2 + 1

    # 처음 중심 공을 auxiliary 바구니로 이동
    print(source, auxiliary)

    # 다음 중심 공을 target 바구니로 이동
    print(source, target)

    # auxiliary 바구니의 중심 공을 target 바구니로 이동
    print(auxiliary, target)

N = int(input())

print(2 ** N - 1)
move_center_ball(N, 1, 2, 3)