# https://engineer-mole.tistory.com/238

def solution(my_string):
    table = my_string.maketrans({
        'a' : '', 
        'e' : '', 
        'i' : '', 
        'o' : '', 
        'u' : ''
    })
    
    answer = my_string.translate(table)
    print(answer)
    
    return answer