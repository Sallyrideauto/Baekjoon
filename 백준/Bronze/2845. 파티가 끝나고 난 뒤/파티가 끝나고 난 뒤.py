L, P = map(int, input().split())  # 1제곱미터당 사람의 수 L과 파티가 열렸던 곳의 넓이 P를 입력받음
attendees = list(map(int, input().split()))  # 각 기사에 실려있는 참가자의 수를 입력받음

total_attendees = L * P  # 상근이가 계산한 참가자의 수
diffs = [a - total_attendees for a in attendees]  # 각 기사에 적혀 있는 참가자의 수와 상근이가 계산한 참가자의 수의 차이를 계산함

for diff in diffs:
    print(diff, end=' ')
