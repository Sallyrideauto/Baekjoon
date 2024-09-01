def compute_hash(s, p, m):
    hash_value = 0
    power = 1
    
    for char in s:
        # 문자를 숫자로 변환(a = 1, b = 2, ..., z = 26)
        char_value = ord(char) - ord('a') + 1
        # 해시값에 현재 문자의 값을 더함
        hash_value = (hash_value + char_value * power) % m
        # 다음 문자를 위한 파워값 계산
        power = (power * p) % m
        
    return hash_value

# 입력 처리
n = int(input())
s = input().strip()
p = 31    # 문제에서 주어진 p값
m = 1234567891    # 문제에서 주어진 m값

# 해시값 계산 및 출력
print(compute_hash(s, p, m))