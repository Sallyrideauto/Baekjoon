from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])  # (중요도, 인덱스) 형태의 튜플을 큐에 저장
    count = 0  # 프로세스 실행 순서를 세는 변수

    while queue:
        current = queue.popleft()  # 큐에서 가장 앞에 있는 프로세스를 꺼냄
        if any(current[0] < p[0] for p in queue):  # 현재 프로세스보다 우선순위가 높은 프로세스가 큐에 남아있는 경우
            queue.append(current)  # 현재 프로세스를 다시 큐에 넣음
        else:  # 현재 프로세스가 가장 우선순위가 높은 경우
            count += 1  # 프로세스 실행 순서를 증가시킴
            if current[1] == location:  # 원하는 프로세스를 찾은 경우
                return count  # 실행 순서를 반환

    return count
