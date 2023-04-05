"""
다음은 입력값을 받고, 챕터를 읽는 데 걸리는 시간과 페이지 수를 리스트로 저장하는 코드입니다.
그 다음에 가능한 모든 챕터 조합을 구한 후, 읽을 수 있는 최대 페이지 수를 구합니다.
"""

import itertools

# 입력 받기
n, m = map(int, input().split())

chapters = []
for i in range(m):
    time, pages = map(int, input().split())
    chapters.append((time, pages))

max_pages = 0

# 가능한 모든 챕터 조합에 대해 최대 페이지 수 구하기
for i in range(1, m+1):
    for subset in itertools.combinations(chapters, i):
        total_time = sum(time for time, _ in subset)
        if total_time <= n:
            total_pages = sum(pages for _, pages in subset)
            max_pages = max(max_pages, total_pages)

print(max_pages)

"""
이 코드는 가능한 모든 챕터 조합에 대해 최대 페이지 수를 구하기 때문에, 
입력값이 크면 연산 시간이 많이 걸릴 수 있습니다. 
하지만, 입력값이 작으면 충분히 빠르게 동작할 것입니다.
"""