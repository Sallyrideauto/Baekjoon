def largestRectangle(heights):
    # 스택 초기화
    stack = []
    # 결과값인 최대 넓이를 0으로 초기화
    max_area = 0

    # 히스토그램의 각 높이에 대해
    for i in range(len(heights)):
        # 스택이 비어 있지 않고, 현재 높이가 스택의 최상위 높이보다 낮은 경우
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            # 스택이 비어 있다면 width는 i, 아니라면 i에서 스택의 최상위 값 - 1을 뺀 값
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        # 현재 높이를 스택에 추가
        stack.append(i)

    # 스택에 남아 있는 높이에 대해
    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

while True:
    # 입력값 받기
    data = list(map(int, input().split()))
    # 입력의 마지막 줄이 0이면 종료
    if data[0] == 0:
        break
    # 첫 번째 입력값은 직사각형의 수이므로 제외하고 나머지를 largestRectangle 함수에 전달
    print(largestRectangle(data[1:]))