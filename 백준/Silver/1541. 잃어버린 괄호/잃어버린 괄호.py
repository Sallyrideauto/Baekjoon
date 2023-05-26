"""
식을 최소로 만들기 위해서는 '+' 연산자 뒤에 오는 숫자를 음수로 만들어야 합니다. 
따라서, '+' 연산자를 기준으로 식을 분할하고, 
각 분할된 식을 순서대로 계산하여 최종 결과를 구하면 됩니다.

알고리즘의 구체적인 단계는 다음과 같습니다:

1. 입력으로 주어진 식에서 '+'를 기준으로 분할하여 각 부분식을 리스트에 저장합니다.
2. 첫 번째 부분식을 결과값으로 초기화합니다.
3. 두 번째 부분식부터 마지막 부분식까지 순서대로 반복하면서, 현재 부분식에 '-' 연산자가 있는 경우 해당 숫자를 음수로 변환합니다.
4. 현재 부분식의 값을 결과값에 더합니다.
5. 최종적으로 구해진 결과값을 출력합니다.
"""

expression = input()  # 식 입력

# '-'를 기준으로 분할하여 부분식 리스트에 저장
subexpressions = expression.split('-')

# 첫 번째 부분식을 결과값으로 초기화
result = sum(map(int, subexpressions[0].split('+')))

# 두 번째 부분식부터 마지막 부분식까지 반복
for subexp in subexpressions[1:]:
    # '+' 연산자가 있는 경우 해당 숫자를 더합니다.
    result -= sum(map(int, subexp.split('+')))

print(result)  # 결과 출력