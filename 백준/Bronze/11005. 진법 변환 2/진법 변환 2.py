n, b = map(int, input().split())

if n == 0:
    print(0)
else:
    answer = ''
    while n > 0:
        # 10진수에서 B진수로 변환하는 방법
        # n을 B로 나눈 나머지를 문자로 변환하여 answer의 앞에 추가한다.
        # n을 B로 나눈 몫을 n으로 갱신한다.
        digit = n % b
        if digit < 10:
            answer = str(digit) + answer
        else:
            answer = chr(ord('A') + digit - 10) + answer
        n //= b
    print(answer)

"""
먼저 입력으로 받은 n과 b를 map() 함수를 사용하여 정수형으로 변환한다. 
n이 0인 경우에는 0을 출력하고, 아닌 경우에는 answer라는 빈 문자열을 만들어서 10진수 n을 B진수로 변환한다. 변환하는 방법은 다음과 같다.

1. n을 b로 나눈 나머지 digit를 구한다.
2. digit가 10보다 작은 경우에는 그대로 문자열로 변환하여 answer의 앞에 추가한다.
3. digit가 10 이상인 경우에는 A부터 순서대로 알파벳 대문자를 사용하여 숫자 10부터 35까지를 표현한다. 
따라서 digit에서 10을 뺀 값을 A의 아스키 코드값에 더한 후, 이를 문자로 변환하여 answer의 앞에 추가한다.
4. n을 b로 나눈 몫을 n으로 갱신한다.
5. 1~4 과정을 n이 0이 될 때까지 반복한다.

위 과정을 거치면 answer에는 10진수 n을 B진수로 변환한 결과가 문자열 형태로 저장된다. 이를 출력한다.
"""