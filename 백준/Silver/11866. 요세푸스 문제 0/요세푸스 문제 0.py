"""
요세푸스 문제는 사람들이 원을 이루며 제거되는 순서를 구하는 문제입니다.
우선 원을 리스트로 구현하고, K번째 사람을 제거하면서 순서대로 리스트를 탐색합니다.
제거되는 사람들은 따로 리스트에 저장하고, 
리스트에서 제거될 때마다 나머지 사람들의 인덱스가 바뀌기 때문에 인덱스를 조정해줘야 합니다.
"""

n, k = map(int, input().split())

# 원 생성
circle = list(range(1, n+1))
result = []

# 인덱스와 리스트 길이 초기화
index = 0
length = len(circle)

# 원에서 사람들이 제거되는 순서 탐색
while length > 0:
    index = (index + k - 1) % length  # k번째 사람의 인덱스 계산
    result.append(circle.pop(index))  # k번째 사람을 제거하고 결과 리스트에 추가
    length -= 1  # 리스트 길이 감소
# 요세푸스 순열 출력
print("<" + ", ".join(map(str, result)) + ">")

"""
우선 입력으로 N과 K를 받아서 원을 생성합니다.
인덱스와 리스트 길이를 초기화한 후, while문을 통해 원에서 사람들이 제거되는 순서를 탐색합니다.
인덱스는 (index + k - 1) % length으로 계산하며, pop() 메소드를 이용해 k번째 사람을 제거하고 결과 리스트에 추가합니다.
제거된 사람은 리스트에서 제거되므로 리스트 길이(length)를 1 감소시킵니다.
모든 사람이 제거되면 결과 리스트를 출력합니다.
"""