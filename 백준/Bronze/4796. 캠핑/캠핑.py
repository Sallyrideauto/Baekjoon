def camping_days(L, P, V):
    quotient, remainder = divmod(V, P)
    return quotient * L + min(remainder, L)

case_number = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    max_days = camping_days(L, P, V)
    print(f"Case {case_number}: {max_days}")
    case_number += 1

"""
이 프로그램은 각 테스트 케이스에 대해 L, P, V를 입력 받고, 
camping_days 함수를 호출하여 최대 사용 가능한 캠핑장 이용 일수를 계산합니다. 
결과를 출력한 후 케이스 번호를 증가시키며 다음 테스트 케이스를 처리합니다. 
입력이 모두 0인 경우 종료합니다.
"""