import sys
import math
from collections import deque

def lcm(a, b):
    """두 수의 최소공배수를 반환"""
    return a * b // math.gcd(a, b)

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    
    # 각 재료(노드)에 연결된 (다음 노드, p, q) 정보를 저장합니다.
    # 입력으로 "A B p q"가 주어지면, A와 B의 비율은 p:q, 즉 A/B = p/q.
    # 한쪽 방향에서는 A를 기준으로 B의 값을 구할 때 (q, p)를, 반대쪽에서는 (p, q)를 사용합니다.
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        A, B, p, q = map(int, input().split())
        # A -> B 방향: 만약 A의 양이 알려져 있다면, B의 양은 A의 양 * (q/p)
        graph[A].append((B, p, q))
        # B -> A 방향: 만약 B의 양이 알려져 있다면, A의 양은 B의 양 * (p/q)
        graph[B].append((A, q, p))
    
    # 각 재료의 양을 (분자, 분모)의 형태로 저장합니다.
    fractions = [None] * N
    fractions[0] = (1, 1)  # 0번 재료를 기준으로 1/1로 시작
    visited = [False] * N
    visited[0] = True

    # DFS를 사용하여 각 재료의 양(분수)를 구합니다.
    stack = [0]
    while stack:
        current = stack.pop()
        num_current, den_current = fractions[current]
        
        for neighbor, p, q in graph[current]:
            if not visited[neighbor]:
                # 주어진 current와 neighbor의 비율: current : neighbor = p : q
                # current의 양이 num_current/den_current라면,
                # neighbor의 양은 (num_current * q) / (den_current * p)
                num_neighbor = num_current * q
                den_neighbor = den_current * p
                
                # 기약분수로 만들기 위해 최대공약수로 나눕니다.
                g = math.gcd(num_neighbor, den_neighbor)
                num_neighbor //= g
                den_neighbor //= g
                
                fractions[neighbor] = (num_neighbor, den_neighbor)
                visited[neighbor] = True
                stack.append(neighbor)
    
    # 모든 분수의 분모들에 대해 최소공배수(LCM)를 구합니다.
    lcm_value = 1
    for num, den in fractions:
        lcm_value = lcm(lcm_value, den)
    
    # LCM을 곱하여 각 재료의 양을 정수로 변환합니다.
    amounts = [0] * N
    for i in range(N):
        num, den = fractions[i]
        amounts[i] = num * (lcm_value // den)
    
    # 모든 정수 양들의 최대공약수(GCD)를 구한 후, 각 양을 나눠 최소 해로 만듭니다.
    gcd_all = amounts[0]
    for a in amounts[1:]:
        gcd_all = math.gcd(gcd_all, a)
    
    amounts = [a // gcd_all for a in amounts]
    
    # 결과 출력
    print(" ".join(map(str, amounts)))

if __name__ == '__main__':
    main()
