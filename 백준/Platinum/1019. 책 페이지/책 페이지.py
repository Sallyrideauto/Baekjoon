def count_digits(n):
    # 숫자의 등장 횟수를 저장할 배열
    count = [0] * 10
    factor = 1
    
    while factor <= n:
        lower_numbers = n - (n // factor) * factor
        current_digit = (n // factor) % 10
        higher_numbers = n // (factor * 10)
        
        # 높은 자릿수에서 올라온 숫자를 모든 숫자에 더함
        for i in range(10):
            count[i] += higher_numbers * factor
        # 0을 고려하여 보정
        count[0] -= factor
        
        # 현재 자릿수의 숫자가 k일 때
        for i in range(current_digit):
            count[i] += factor
        count[current_digit] += lower_numbers + 1
            
        factor *= 10
        
    return count
    
n = int(input())
result = count_digits(n)
print(" ".join(map(str, result)))