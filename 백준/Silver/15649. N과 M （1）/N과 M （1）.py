from itertools import permutations

n, m = map(int, input().split())

# 1부터 N까지 수열 생성
numbers = [i for i in range(1, n+1)]

# 길이가 M인 순열 생성
perms = permutations(numbers, m)

# 모든 순열 출력
for perm in perms:
    print(' '.join(map(str, perm)))
