'''
제공된 코드는 입력된 수에서 중복을 제거하고 있어서 문제의 요구사항에 맞지 않습니다.
문제는 중복된 수를 포함하여 정렬을 수행한 후 K번째 있는 수를 찾으라고 요구하고 있습니다.

또한, N의 크기가 최대 5,000,000까지이고 각 요소의 크기가 -10^9에서 10^9 사이이므로,
효율적인 정렬 알고리즘을 사용해야 시간 제한 내에 문제를 해결할 수 있습니다.
파이썬의 기본 정렬 함수인 sorted()는 효율적인 정렬 알고리즘(Timsort)을 사용하기 때문에 시간 제한에 적합합니다.
'''

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
sorted_num = sorted(numbers) # 중복을 제거하지 않고 오름차순으로 정렬

print(sorted_num[K - 1])