from collections import deque

def find_print_order(num_docs, target_idx, docs_priority):
    docs = deque([(i, p) for i, p in enumerate(docs_priority)])
    cnt = 0
    
    while docs:
        doc = docs.popleft()
        if docs and max(docs, key=lambda x: x[1])[1] > doc[1]:
            docs.append(doc)
        else:
            cnt += 1
            if doc[0] == target_idx:
                return cnt

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    print(find_print_order(n, m, priorities))

"""
이 프로그램은 테스트 케이스의 개수 t를 입력 받고, 
각 테스트 케이스마다 문서의 개수 n, 
몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 m, 
그리고 n개 문서의 중요도를 입력 받습니다.

find_print_order 함수는 문서의 개수 num_docs, 
몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 target_idx, 
그리고 num_docs개 문서의 중요도가 리스트 docs_priority로 주어집니다.

이 함수에서는 docs라는 이름의 deque 자료구조를 이용하여, 문서들을 순서대로 처리합니다. 
docs deque의 각 원소는 문서의 인덱스와 중요도로 구성되어 있습니다.

cnt 변수는 현재까지 인쇄된 문서의 개수를 나타내며, 반복문을 돌면서 문서를 하나씩 처리합니다. 
먼저 deque의 왼쪽에서 하나의 문서를 뽑아내고, 나머지 문서들 중에서 현재 문서의 중요도보다 높은 중요도를 가진 문서가 있는지 확인합니다. 
만약 그러한 문서가 있다면, 현재 문서를 deque의 오른쪽 끝에 다시 넣어줍니다. 
그렇지 않으면 현재 문서를 인쇄하고, cnt를 1 증가시킵니다. 
이 때, 현재 문서의 인덱스가 target_idx와 같다면, 현재까지 인쇄된 문서의 개수 cnt를 반환합니다.

마지막으로, 입력 받은 테스트 케이스에 대해 find_print_order 함수를 호출하여 결과를 출력합니다.
"""