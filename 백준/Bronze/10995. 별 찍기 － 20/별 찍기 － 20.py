# https://hooneee.tistory.com/230

N = int(input())

for i in range(1, N + 1):
    if i % 2:
        print("* " * N)
    else:
        print(" *" * N)