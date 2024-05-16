import heapq

def solution(scoville, K):
    # 최소 힙으로 변환
    heapq.heapify(scoville)
    
    count = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        # 가장 작은 두 개의 음식을 섞음
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_food = first + (second * 2)
        heapq.heappush(scoville, new_food)
        
        count += 1
        
    return count