# https://hkim-data.tistory.com/179
# 2의 제곱수와 완전제곱수의 차이 정리하기

def isPowerOfTwo(N):
    if N != 0 and (N & (N - 1)) == 0:
        return 1
    else:
        return 0

N = int(input())
print(isPowerOfTwo(N))