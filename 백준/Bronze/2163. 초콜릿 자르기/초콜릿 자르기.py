"""
이 문제는 초콜릿을 1×1 크기로 쪼개는 데 필요한 최소 횟수를 찾는 것입니다. 
이를 해결하기 위한 아이디어는 간단합니다. 
우리는 먼저 초콜릿을 세로로 쪼개고, 그 다음 각 조각을 가로로 쪼개면 됩니다. 
이 경우, 총 쪼개는 횟수는 (N-1) + N*(M-1)이 됩니다. 
이는 먼저 N-1번 세로로 쪼개서 N개의 조각을 만들고, 각 조각을 M-1번 가로로 쪼개는 것입니다.
"""

N, M = map(int, input().split())
print((N-1) + N*(M-1))

"""
이 코드는 첫째 줄에서 두 정수 N, M을 입력 받고, 
그 다음 줄에서 위에서 설명한 공식을 사용하여 최소 쪼개기 횟수를 출력합니다.
"""