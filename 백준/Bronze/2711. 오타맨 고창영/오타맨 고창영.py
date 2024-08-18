n = int(input())

for _ in range(n):
    idx, s = input().split()
    idx = int(idx)
    s = s[:idx - 1] + s[idx:]
    print(s)