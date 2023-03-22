import math

A, B, V = map(int, input().split())

day = math.ceil((V - B) / (A - B))

print(day)

"""
달팽이는 낮 동안 A미터를 올라가고 밤 동안 B미터를 내려오므로, 하루에 올라가는 거리는 A-B미터이다. 
따라서 목표 지점 V까지 가려면 총 (V-B) / (A-B)일이 걸리게 된다. 
여기서 소수점이 나오는 경우, 다음 날부터 올라가기 때문에 올림 처리를 해주어야 한다. 
따라서 math 모듈의 ceil 함수를 사용하여 결과를 출력한다.
"""