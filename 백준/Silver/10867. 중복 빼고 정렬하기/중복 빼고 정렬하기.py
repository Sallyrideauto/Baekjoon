'''
set을 사용하여 숫자들의 중복을 제거한 후, 이를 다시 리스트로 변환하였지만, set은 자동으로 정렬을 보장하지 않습니다.
따라서 정렬되지 않은 상태의 리스트가 되므로, sorted 함수를 사용하여 리스트를 오름차순으로 정렬해야 합니다.
'''

N = int(input())
numbers = list(map(int, input().split()))
sorted_num = sorted(list(set(numbers))) # 오름차순으로 정렬

for elem in sorted_num:
    print(elem, end = ' ')