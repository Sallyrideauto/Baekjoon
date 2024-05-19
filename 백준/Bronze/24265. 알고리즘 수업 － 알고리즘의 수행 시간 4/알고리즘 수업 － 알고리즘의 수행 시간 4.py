def men_of_passion(n):
    # 수행 횟수 계산
    operations = (n - 1) * n // 2
    
    # 최고차항의 차수는 2(n^2의 항이 존재하므로)
    degree_of_polynomial = 2
    
    return operations, degree_of_polynomial

n = int(input())
operations, degree_of_polynomial = men_of_passion(n)

print(operations)
print(degree_of_polynomial)