# 주어진 규칙에 따라 수열을 생성한 다음, 주어진 구간에 속하는 숫자의 합을 구하는 함수를 작성

def create_sequence():
    sequence = []
    num = 1

    while len(sequence) < 1000:
        sequence.extend([num] * num)
        num += 1

    return sequence

def sum_of_subsequence(sequence, a, b):
    return sum(sequence[a-1:b])

def main():
    a, b = map(int, input().split())
    sequence = create_sequence()
    result = sum_of_subsequence(sequence, a, b)
    print(result)

if __name__ == "__main__":
    main()

"""
이 프로그램은 구간의 시작과 끝을 나타내는 정수 A와 B를 입력으로 받아서 수열에서 A번째 숫자부터 B번째 숫자까지 합을 구하고 출력합니다. 
수열은 주어진 규칙에 따라 생성되며, create_sequence 함수를 사용하여 생성됩니다. 
sum_of_subsequence 함수는 주어진 수열과 구간을 사용하여 해당 구간의 합을 계산합니다.
"""