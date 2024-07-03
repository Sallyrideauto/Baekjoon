from itertools import combinations

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
    
def calculate_chicken_distance(houses, chicken_stores):
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in chicken_stores:
            distance = manhattan_distance(hx, hy, cx, cy)
            if distance < min_distance:
                min_distance = distance
        total_distance += min_distance
    return total_distance
    
def solve():
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    
    houses = []
    chickens = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                chickens.append((i, j))
                
    # 모든 치킨집 조합을 생성
    min_chicken_distance = float('inf')
    for chicken_comb in combinations(chickens, M):
        # 현재 조합에 대한 치킨 거리를 계산
        chicken_distance = calculate_chicken_distance(houses, chicken_comb)
        if chicken_distance < min_chicken_distance:
            min_chicken_distance = chicken_distance
            
    print(min_chicken_distance)
    
if __name__ == "__main__":
    solve()