def solution(array):
    counts = [0] * 1000  # 각 수의 출현 횟수를 저장할 배열
    max_count = 0  # 가장 많이 출현한 수의 출현 횟수
    max_num = -1  # 가장 많이 출현한 수

    # 각 수의 출현 횟수를 센다.
    for num in array:
        counts[num] += 1

    # 가장 많이 출현한 수를 찾는다.
    for num in range(1000):
        if counts[num] > max_count:
            max_count = counts[num]
            max_num = num

    # 최빈값이 여러 개면 -1을 리턴한다.
    for num in range(1000):
        if counts[num] == max_count and num != max_num:
            return -1

    return max_num