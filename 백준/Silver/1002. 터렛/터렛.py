import math

t = int(input())
results = []

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    if dist == 0 and r1 == r2:
        results.append(-1)
    elif abs(r1 - r2) < dist < (r1 + r2):
        results.append(2)
    elif dist == r1 + r2 or dist == abs(r1 - r2):
        results.append(1)
    else:
        results.append(0)
        
for result in results:
    print(result)