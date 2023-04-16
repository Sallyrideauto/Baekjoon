def can_convert(S, T):
    while len(S) < len(T):
        if T[-1] == 'A':
            T = T[:-1]
        elif T[-1] == 'B':
            T = T[:-1][::-1]
        else:
            return False
    return S == T

def main():
    S = input().strip()
    T = input().strip()
    result = can_convert(S, T)
    print(1 if result else 0)

if __name__ == "__main__":
    main()

"""
이 프로그램은 두 문자열 S와 T를 입력 받아 주어진 연산을 사용하여 S를 T로 변환할 수 있는지 확인한 후, 
가능하면 1을, 불가능하면 0을 출력합니다. 
입력된 문자열을 사용하여 프로그램을 실행하면 S를 T로 변환할 수 있는지 여부를 출력합니다.
"""