def solution(progresses, speeds):
    answer = []
    days = []  # 작업이 완료되는데 걸리는 일수를 저장하는 리스트

    # 작업이 완료되는데 걸리는 일수 계산
    for i in range(len(progresses)):
        remaining = 100 - progresses[i]
        day = remaining // speeds[i]  # 나눗셈의 몫 계산
        if remaining % speeds[i] != 0:  # 나눗셈의 나머지가 있으면 하루 더 필요
            day += 1
        days.append(day)

    count = 0  # 배포되는 기능의 수를 세는 변수
    max_day = days[0]  # 가장 오래 걸리는 일수 초기화

    for day in days:
        if day <= max_day:  # 이전에 배포될 기능과 같이 배포 가능한 경우
            count += 1
        else:  # 이전에 배포될 기능보다 더 오래 걸리는 경우
            answer.append(count)
            count = 1
            max_day = day

    answer.append(count)  # 마지막 배포되는 기능의 수 추가

    return answer