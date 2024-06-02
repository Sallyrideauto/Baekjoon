def combination(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = den = 1
    for i in range(k):
        num *= (n - i)
        den *= (i + 1)
    return num // den
    
def count_ways(N):
    if N < 9 or N % 3 != 0:
        return 0
    k = N // 3
    return combination(k - 1, 2)    # k - 3 + 2 = k - 1에서 2를 선택
    
N = int(input())
result = count_ways(N)
print(result)