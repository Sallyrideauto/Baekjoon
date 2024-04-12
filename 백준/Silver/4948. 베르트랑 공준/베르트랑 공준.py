# 에라토스테네스의 체 알고리즘을 사용하여 소수를 효율적으로 탐색

def count_prime(n):
    sieve = [True] * (2 * n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int((2 * n) ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, 2 * n + 1, i):
                sieve[j] = False
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if sieve[i]:
            count += 1
    return count

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        print(count_prime(n))
        
if __name__ == '__main__':
    main()