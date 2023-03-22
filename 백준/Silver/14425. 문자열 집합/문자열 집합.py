"""
아래는 입력받은 문자열을 집합(set)으로 만든 뒤, 
검사해야 하는 문자열을 하나씩 집합에 포함되어 있는지 
확인하는 방식으로 구현한 예시 코드입니다.
"""

N, M = map(int, input().split())
s = set(input().strip() for _ in range(N))
count = 0
for _ in range(M):
    if input().strip() in s:
        count += 1
print(count)

"""
입력받은 문자열을 set으로 만들어서 검사해야 하는 문자열이 
집합에 포함되어 있는지 확인하기 때문에 시간 복잡도는 O(N+M)입니다.
"""