import sys

n, m = map(int, sys.stdin.readline().split())

hear = set()
see = set()

for i in range(n):
    hear.add(sys.stdin.readline().rstrip())

for j in range(m):
    see.add(sys.stdin.readline().rstrip())

# 듣도 보도 못한 사람의 명단을 구한다
hear_see = sorted(list(hear & see))

# 듣보잡 수와 명단을 출력한다
print(len(hear_see))
for name in hear_see:
    print(name)

"""
듣도 못한 사람과 보도 못한 사람을 따로 set() 자료형으로 저장합니다.
set() 자료형의 교집합 연산을 사용하여 듣보잡의 명단을 구합니다.
명단을 알파벳 순서대로 정렬하고 출력합니다.
"""