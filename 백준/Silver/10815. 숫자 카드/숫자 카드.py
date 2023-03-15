n = int(input())
cards = set(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

for num in numbers:
    if num in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
