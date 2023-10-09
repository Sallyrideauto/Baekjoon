'''
https://1ets-just-do-it.tistory.com/53

arr1 = [
    list(map(int, input().split()))
    for _ in range(2)
]

arr2 = [
    list(map(int, input().split()))
    for _ in range(2)
]

print(arr1, arr2)
new_arr = []

for i in range(len(arr1)):
    sum_val = 0
    for j in range(len(arr2)):
        sum_val = arr1[i][j] + arr2[i][j]
    new_arr.append(sum_val)

print(new_arr)
'''

def solution(arr1, arr2):
    result = []
    
    for a, b in zip(arr1, arr2):
        sum = []
        for i, j in zip(a, b):
            sum.append(i + j)
        result.append(sum)
        
    return result