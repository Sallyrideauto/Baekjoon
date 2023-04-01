# 각 숫자를 생성자로 사용하여 d(n)의 결과로 나오는 수들을 모두 구하고, 그 중에서 1~10,000까지의 수들을 제외한 나머지 수들을 출력하면 됩니다.

def d(n):
    return n + sum(map(int, str(n)))

self_numbers = set(range(1, 10001)) # 1~10,000 사이의 모든 수를 집합에 추가

for i in range(1, 10001):
    generated_num = d(i)
    if generated_num in self_numbers:
        self_numbers.remove(generated_num) # 생성자로부터 생성된 수들을 집합에서 제거

for num in sorted(self_numbers):
    print(num)

"""
위 코드에서 d(n) 함수는 주어진 수 n과 n의 각 자리수를 더한 값을 반환합니다. 
이 함수를 이용하여 1부터 10,000까지의 모든 수에 대해 d(n) 함수를 적용한 결과를 구하고, 
이 결과값이 1부터 10,000까지의 수 중 하나에 해당되면 해당 수를 집합에서 제거합니다. 
마지막으로 집합에 남은 모든 수들을 정렬하여 출력하면 됩니다.
"""