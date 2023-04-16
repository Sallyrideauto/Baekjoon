from collections import deque

def pour_water(A, B, C):
    visited = set()
    possible = set()

    q = deque([(0, 0, C)])

    while q:
        a, b, c = q.popleft()

        if (a, b, c) not in visited:
            visited.add((a, b, c))

            if a == 0:
                possible.add(c)

            # Pour water from c to a
            if a + c > A:
                q.append((A, b, c - (A - a)))
            else:
                q.append((a + c, b, 0))

            # Pour water from c to b
            if b + c > B:
                q.append((a, B, c - (B - b)))
            else:
                q.append((a, b + c, 0))

            # Pour water from a to c
            if a + c > C:
                q.append((a - (C - c), b, C))
            else:
                q.append((0, b, a + c))

            # Pour water from a to b
            if a + b > B:
                q.append((a - (B - b), B, c))
            else:
                q.append((0, a + b, c))

            # Pour water from b to c
            if b + c > C:
                q.append((a, b - (C - c), C))
            else:
                q.append((a, 0, b + c))

            # Pour water from b to a
            if b + a > A:
                q.append((A, b - (A - a), c))
            else:
                q.append((a + b, 0, c))

    return sorted(possible)

def main():
    A, B, C = map(int, input().split())
    result = pour_water(A, B, C)
    print(*result)

if __name__ == "__main__":
    main()

"""
이 프로그램은 세 개의 물통에서 물을 쏟아 부으면서 첫 번째 물통이 비어 있을 때 세 번째 물통에 담겨있을 수 있는 물의 양을 모두 구하고, 
오름차순으로 정렬하여 출력합니다. 
주어진 입력을 사용하여 프로그램을 실행하면 가능한 세 번째 물통의 용량을 계산하고 출력합니다.
"""