# 입력값을 받아 절단기의 최대 높이를 이분탐색으로 구하는 파이썬 코드

n, m = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)

while left <= right:
    mid = (left + right) // 2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    if total >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)

"""
첫번째 줄에서는 나무의 수와 상근이가 집으로 가져가려고 하는 나무의 길이 M을 입력받습니다.

두번째 줄에서는 각 나무의 높이를 입력받습니다.

이분탐색을 위해 left와 right를 설정합니다. 
left는 0으로, right는 나무 중 가장 높은 나무의 높이로 설정합니다.

while문에서 이분탐색을 수행합니다. 
이분탐색의 종료 조건은 left > right일 때입니다. 
이때, 최대 높이는 right입니다.

이분탐색의 핵심은 mid입니다. 
mid는 left와 right의 중간값입니다. 
mid를 기준으로 나무를 자르고, 이 자른 나무의 길이가 M 이상이 되는지 검사합니다.

나무를 자르는 것은 for loop 안에서 수행합니다. 
만약 나무의 높이가 mid보다 크다면, 그 나무에서 mid만큼 잘라냅니다. 
이렇게 자른 나무의 길이를 total에 더합니다.

total이 M 이상이라면, left를 mid+1로 이동시켜서 높이를 높여서 자르는 것을 수행합니다. 
total이 M보다 작다면, right를 mid-1로 이동시켜서 높이를 낮춰서 자르는 것을 수행합니다.

최종적으로 right를 출력합니다.
"""