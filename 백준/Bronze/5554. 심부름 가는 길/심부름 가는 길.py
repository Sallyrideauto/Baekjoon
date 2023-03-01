# 집에서 학교까지 이동 시간 입력
time_to_school = int(input())

# 학교에서 PC방까지 이동 시간 입력
time_to_pc = int(input())

# PC방에서 학원까지 이동 시간 입력
time_to_academy = int(input())

# 학원에서 집까지 이동 시간 입력
time_to_home = int(input())

# 총 이동 시간 계산
total_time = time_to_school + time_to_pc + time_to_academy + time_to_home

# 분과 초 계산
minutes = total_time // 60
seconds = total_time % 60

# 출력
print(minutes)
print(seconds)
