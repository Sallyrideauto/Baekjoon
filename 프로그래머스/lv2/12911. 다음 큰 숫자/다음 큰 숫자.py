def solution(n):
    binary_n = bin(n)[2:]
    count_n = binary_n.count('1')
    while True:
        n += 1
        binary_next = bin(n)[2:]
        count_next = binary_next.count('1')
        if count_next == count_n:
            return n
