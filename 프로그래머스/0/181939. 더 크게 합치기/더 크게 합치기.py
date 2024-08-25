def solution(a, b):
    a, b = str(a), str(b)

    a_add_b = a + b
    b_add_a = b + a
    
    a_add_b, b_add_a = int(a_add_b), int(b_add_a)
    
    if a_add_b > b_add_a:
        return a_add_b
    elif a_add_b < b_add_a:
        return b_add_a
    else:
        return a_add_b