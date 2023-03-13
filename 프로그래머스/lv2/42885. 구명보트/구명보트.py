def solution(people, limit):
    people.sort()  # 오름차순으로 정렬
    i, j = 0, len(people) - 1  # 인덱스 설정
    count = 0  # 필요한 구명보트 수
    while i <= j:
        count += 1  # 구명보트 수 추가
        if people[j] + people[i] <= limit:
            i += 1  # 무게가 가장 적은 사람을 태움
        j -= 1  # 무게가 가장 많은 사람을 태움
    return count