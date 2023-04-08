def is_palindrome(string):
    return string == string[::-1]

def min_palindromes(string):
    n = len(string)
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for j in range(i):
            if is_palindrome(string[j:i]):
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n]

string = input().strip()
print(min_palindromes(string))

"""
먼저 is_palindrome 함수는 주어진 문자열이 팰린드롬인지 아닌지를 확인하는 함수입니다. 
문자열의 슬라이싱과 비교 연산자를 이용하여 문자열을 뒤집어 비교합니다.

min_palindromes 함수는 주어진 문자열을 최소 개수의 팰린드롬으로 나누는 함수입니다. 
우선 문자열의 길이 n을 구합니다. 
dp라는 리스트를 만들어서 dp[i]는 문자열의 처음부터 i번째 문자까지의 부분문자열을 최소 개수의 팰린드롬으로 나눌 때 필요한 최소 팰린드롬의 개수를 나타냅니다. 
dp[0]는 빈 문자열을 나눌 때 필요한 최소 팰린드롬의 개수이므로 0으로 초기화합니다.

이제 문자열의 각 위치 i에 대해서 dp[i]를 구합니다. 
j를 0부터 i-1까지 반복하면서 string[j:i]가 팰린드롬인 경우를 찾습니다. 
이때 dp[i]를 dp[j] + 1과 비교하여 더 작은 값으로 갱신합니다. 
마지막으로 dp[n]을 반환합니다.

마지막으로 input() 함수를 이용하여 문자열을 입력받고, min_palindromes 함수를 호출하여 최소 개수의 팰린드롬을 출력합니다.
"""