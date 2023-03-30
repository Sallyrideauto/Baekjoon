n, b = input().split()
b = int(b)
decimal = 0
for i, digit in enumerate(n[::-1]):
    if digit.isdigit():
        decimal += int(digit) * (b ** i)
    else:
        decimal += (ord(digit) - 55) * (b ** i)
print(decimal)

"""
이 코드는 입력으로 받은 B진법 수 N을 10진법으로 변환하는 프로그램입니다. 
입력으로 받은 B를 정수형으로 바꾸고, B진법 수 N의 각 자리 숫자를 오른쪽부터 하나씩 가져와서 10진법으로 변환한 후, 10진법 수에 더해줍니다. 
이 때, 알파벳 대문자는 ord() 함수를 이용하여 숫자로 변환합니다. 
최종적으로 10진법 수를 출력합니다.
"""