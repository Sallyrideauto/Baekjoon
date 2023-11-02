'''
문제를 다시 살펴보면, 
찬솔이가 지하철 승강장에 도착하는데 걸리는 시간 N과 지하철이 도착하는 시간 B를 더해서 지하철이 오기까지 전체 시간을 계산해야 합니다. 
따라서 지하철 탑승 시간은 N + B가 아니라 N + B - N 즉, B와 같습니다.
'''

N, A, B = map(int, input().split())

if A < B:
    print("Bus")
elif A > B:
    print("Subway")
else:    # A == B
    print("Anything")