import heapq
import sys

def min_heap_operations(ops):
    min_heap = []   # 최소 힙 초기화
    result = []     # 출력 결과를 저장할 리스트

    for _ in range(n):
        x = int(sys.stdin.readline())
        if x == 0:
            if min_heap:
                result.append(str(heapq.heappop(min_heap)))
            else:
                result.append('0')
        else:
            heapq.heappush(min_heap, x)

    return '\n'.join(result)

n = int(input())    # 연산의 개수
print(min_heap_operations(n))