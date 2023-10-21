def solution(d, budget):
    d.sort() # 부서별 신청 금액을 오름차순으로 정렬
    count = 0 # 지원 가능한 부서의 수
    for request in d:
        if budget >= request:
            budget -= request
            count += 1
        else:
            break
    return count