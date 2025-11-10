T = int(input())

for x in range(1, T + 1):
    a, b = map(int, input().split())
    total = a + b
    print(f"Case {x}: {total}")