def solution(arr):
    # 유클리드 알고리즘을 이용하여 최대공약수를 계산하는 함수
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    lcm = arr[0] # 초기값 설정
    for i in range(1, len(arr)):
        # 두 수의 최소공배수 공식을 이용하여 lcm 계산
        lcm = lcm * arr[i] // gcd(lcm, arr[i])
    return lcm