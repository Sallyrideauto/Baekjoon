N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr = A + B
arr = sorted(arr)

for elem in arr:
    print(elem, end = ' ')