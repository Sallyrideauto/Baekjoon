n = int(input())  # 출입 기록 수
logs = []  # 출입 기록 저장할 리스트

for _ in range(n):
    record = input().split()  # 출입 기록 입력 받기
    name, action = record[0], record[1]  # 이름과 출입 동작
    logs.append((name, action))  # 출입 기록 리스트에 추가

# 현재 회사에 있는 사람들을 찾아내기
current_employees = set()
for log in logs:
    name, action = log[0], log[1]
    if action == "enter":
        current_employees.add(name)
    elif action == "leave":
        current_employees.remove(name)

# 사전 순의 역순으로 출력
sorted_employees = sorted(current_employees, reverse=True)
for employee in sorted_employees:
    print(employee)