while True:
    num = input()
    if num == '0':
        break
    
    if num == num[::-1]:
        print('yes')
    else:
        print('no')

"""
입력을 받아서 입력이 0 이 아니면서 팰린드롬인지를 검사합니다.
입력을 뒤집은 값([::-1])과 원래 값이 같으면 팰린드롬이므로 'yes' 를 출력합니다.
팰린드롬이 아니면 'no' 를 출력합니다.
입력이 0 이면 프로그램을 종료합니다.
"""