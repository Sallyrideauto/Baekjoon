def reverse_number(x):
    # 숫자를 문자열로 변환하고 뒤집은 후 다시 정수로 변환
    return int(str(x)[::-1])

def main():
    # 두 수 입력 받기
    x, y = map(int, input().split())
    
    # 두 수를 각각 뒤집기
    rev_x = reverse_number(x)
    rev_y = reverse_number(y)
    
    # 뒤집은 숫자들을 더하고 그 결과를 다시 뒤집기
    result = reverse_number(rev_x + rev_y)
    
    print(result)
    
main()