import sys
import statistics

arr = []

for _ in range(5):
    arr.append(int(sys.stdin.readline()))

print(sum(arr) // len(arr))
print(statistics.median(arr))