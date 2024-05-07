def count_crossings(x1, y1, x2, y2, circles):
    crossings = 0
    for cx, cy, r in circles:
        # 시작점과 원 중심간의 거리
        dist1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
        # 도착점과 원 중심간의 거리
        dist2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
        r2 = r ** 2
        # 한 점만 원 내부에 있을 경우
        if (dist1 < r2) != (dist2 < r2):
            crossings += 1
    return crossings

def solve():
    T = int(input())
    results = []
    for _ in range(T):
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())
        circles = []
        for _ in range(n):
            cx, cy, r = map(int, input().split())
            circles.append((cx, cy, r))
        result = count_crossings(x1, y1, x2, y2, circles)
        results.append(result)
    for result in results:
        print(result)

# 아래 코드로 solve 함수를 호출합니다.
if __name__ == "__main__":
    solve()
