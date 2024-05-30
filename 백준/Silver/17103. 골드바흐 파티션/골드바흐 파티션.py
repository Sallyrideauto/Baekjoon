def sieve(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    is_prime[0], is_prime[1] = False, False
    return [p for p in range(n + 1) if is_prime[p]]
    
def goldbach_partitions(n, primes, is_prime):
    count = 0
    for prime in primes:
        if prime > n // 2:
            break
        if is_prime[n - prime]:
            count += 1
    return count
    
# Main Execution
LIMIT = 1000000
primes = sieve(LIMIT)
is_prime = [False] * (LIMIT + 1)
for prime in primes:
    is_prime[prime] = True
    
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    results.append(goldbach_partitions(n, primes, is_prime))
    
for result in results:
    print(result)