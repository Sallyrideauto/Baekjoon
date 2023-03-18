n = int(input())

for i in range(max(n - 54, 1), n):
    if i + sum(map(int, str(i))) == n:
        print(i)
        break
else:
    print(0)
