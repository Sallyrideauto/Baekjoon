"""
이 문제는 한수를 찾는 문제입니다. 
한수는 자신의 각 자리수가 등차수열을 이룬다는 조건을 만족하는 수를 말합니다. 
즉, 각 자리수의 차이가 일정하다는 것을 의미합니다.

이 문제는 각 자리수의 차이를 비교해야 하므로, 각 자리수를 얻기 위해 문자열로 변환하는 접근 방식이 필요합니다.
"""

def is_hansu(n):
    n_str = str(n)
    if len(n_str) < 3:  # 1자리수와 2자리수는 모두 한수입니다.
        return True
    else:  # 3자리수 이상에서는 등차수열인지 확인합니다.
        diff = int(n_str[1]) - int(n_str[0])
        for i in range(2, len(n_str)):
            if int(n_str[i]) - int(n_str[i-1]) != diff:
                return False
        return True

N = int(input())
count = 0
for i in range(1, N+1):
    if is_hansu(i):
        count += 1

print(count)

"""
이 코드는 입력된 수 N에 대해 1부터 N까지의 각 수에 대해 한수인지 판단하는 함수를 적용하고, 한수인 경우 카운트를 증가시킵니다. 
모든 수를 검사한 후에는 한수의 개수를 출력합니다.
"""