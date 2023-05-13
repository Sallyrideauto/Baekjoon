def solution(n, lost, reserve):
    students = [1] * (n + 1)  # 학생들의 체육복 상태를 나타내는 리스트 (1로 초기화)

    # 체육복 도난당한 학생들 표시
    for l in lost:
        students[l] -= 1

    # 여벌 체육복 가져온 학생들 표시
    for r in reserve:
        students[r] += 1

    # 체육복 빌려주기
    for i in range(1, n + 1):
        if students[i] == 0:  # 체육복이 없는 학생일 경우
            if i > 1 and students[i - 1] == 2:  # 앞 번호 학생이 여벌 체육복을 가지고 있는 경우
                students[i] += 1
                students[i - 1] -= 1
            elif i < n and students[i + 1] == 2:  # 뒷 번호 학생이 여벌 체육복을 가지고 있는 경우
                students[i] += 1
                students[i + 1] -= 1

    # 체육수업을 들을 수 있는 학생 수 카운트
    count = 0
    for i in range(1, n + 1):
        if students[i] >= 1:  # 체육복을 가진 학생
            count += 1

    return count