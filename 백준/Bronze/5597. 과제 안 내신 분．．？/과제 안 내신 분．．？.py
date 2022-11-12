students = [False for i in range(30)]

for i in range(28):
    n = int(input())
    students[n - 1] = True

for i in range(30):
    if not students[i]:
        print(i + 1)