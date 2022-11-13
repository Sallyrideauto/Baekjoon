numbers = []
odd = []

for i in range(7):
    n = int(input())
    numbers.append(n)

for i in range(len(numbers)):
    if numbers[i] % 2 == 1:
        odd.append(numbers[i])

if len(odd) != 0:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)