num = input()  # 수를 문자열로 입력받음
sorted_num = sorted(num, reverse=True)  # 문자열을 역순으로 정렬
result = ''.join(sorted_num)  # 정렬된 문자열을 다시 하나의 문자열로 합침

print(result)