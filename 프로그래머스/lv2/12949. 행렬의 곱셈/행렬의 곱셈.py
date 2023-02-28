import numpy as np

def solution(arr1, arr2):
    # arr1과 arr2를 NumPy 배열로 변환
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    # arr1과 arr2를 곱하여 결과 변환
    answer = np.dot(arr1, arr2)
    return answer.tolist()