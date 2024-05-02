from sys import stdin, stdout
from collections import deque
import sys
input = stdin.readline

def solve():
    # 테스트 케이스의 수 입력 받기
    T = int(input().strip())
    results = []
    
    for _ in range(T):
        N, K = map(int, input().strip().split())
        # 각 건물을 짓는 데 필요한 시간
        building_times = list(map(int, input().strip().split()))
        
        # 그래프 초기화
        graph = [[] for _ in range(N + 1)]
        # 각 노드의 진입 차수
        indegree = [0] * (N + 1)
        # dp 배열, 각 노드를 완성하는 데 걸리는 최소 시간
        dp = [0] * (N + 1)
        
        for _ in range(K):
            X, Y = map(int, input().strip().split())
            graph[X].append(Y)
            indegree[Y] += 1
        
        # 목표 건물
        W = int(input().strip())
        
        # 위상 정렬을 위한 큐
        queue = deque()
        
        # 진입 차수가 0인 노드를 큐에 추가
        for i in range(1, N + 1):
            if indegree[i] == 0:
                queue.append(i)
                dp[i] = building_times[i - 1]
        
        # 위상 정렬 수행
        while queue:
            current = queue.popleft()
            
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                
                # 다이나믹 프로그래밍 업데이트
                dp[neighbor] = max(dp[neighbor], dp[current] + building_times[neighbor - 1])
        
        # 결과 저장
        results.append(dp[W])
    
    # 모든 결과 출력
    for result in results:
        stdout.write(str(result) + '\n')

if __name__ == "__main__":
    solve()