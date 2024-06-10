def men_of_passion_count(n):
    # 코드 1의 수행 횟수 계산
    performance_count = n ** 3
    # 최고차항의 차수는 3, n**3이기 때문에
    highest_term_degree = 3
    return performance_count, highest_term_degree
    
n = int(input())
output = men_of_passion_count(n)

print(output[0])
print(output[1])