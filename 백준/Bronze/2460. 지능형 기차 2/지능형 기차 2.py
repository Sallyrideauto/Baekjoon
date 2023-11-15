passengers = []

passenger = 0  # 현재 기차에 탑승한 승객 수

for _ in range(10):
    out, ridein = map(int, input().split())
    passenger -= out    # 현재 기차에 탑승한 승객에서 내린 사람 수 빼기
    passenger += ridein # 내린 자리에 새로 탑승한 사람 수 더하기
    passengers.append(passenger)    # 각 역에서 승객 수 리스트 추가

print(max(passengers))