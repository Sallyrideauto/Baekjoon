binary = input()

decimal = int(binary, 2)
octal = oct(decimal)[2:]

print(octal)

"""
위 코드는 입력으로 주어진 2진수를 int 함수를 사용하여 10진수로 변환한 후, 
oct 함수를 사용하여 8진수로 변환합니다. 변환된 8진수를 출력합니다.
"""