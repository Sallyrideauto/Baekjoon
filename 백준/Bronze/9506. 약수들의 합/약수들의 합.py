while True:
    n = int(input())
    if n == -1:
        break
    
    divisors = [1]
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    
    if sum(divisors) == n:
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")
