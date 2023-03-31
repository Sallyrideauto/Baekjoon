a, b = map(int, input().split())

# 최대공약수 구하기
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

gcd_value = gcd(a, b)

# 최소공배수 구하기
lcm_value = a * b // gcd_value

print(gcd_value)
print(lcm_value)

# 최대공약수는 유클리드 호제법을 사용하여 구하였고, 최소공배수는 두 수의 곱을 최대공약수로 나누어 구하였습니다.