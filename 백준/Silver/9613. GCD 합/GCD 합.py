from math import gcd

def solve():
    t = int(input().strip())
    results = []
    
    for _ in range(t):
        case = list(map(int, input().strip().split()))
        n = case[0] # 첫 번째 수는 숫자의 개수를 의미
        numbers = case[1:]  # 이후의 수들이 실제 계산 대상
        sum_gcd = 0

        # 모든 쌍의 최대공약수 계산
        for i in range(n):
            for j in range(i + 1, n):
                sum_gcd += gcd(numbers[i], numbers[j])
                
        results.append(sum_gcd)
        
    for result in results:
        print(result)
        
solve()