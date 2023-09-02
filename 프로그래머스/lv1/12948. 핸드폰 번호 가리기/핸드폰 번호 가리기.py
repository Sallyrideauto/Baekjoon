def solution(phone_number):
    phone_number = list(phone_number)
    leng = len(phone_number)
    
    front_num = phone_number[:leng - 4]
    back_num = phone_number[leng - 4:]
    
    new_front = []
    
    for elem in front_num:
        new_front.append('*')
    
    phone_number = new_front + back_num
    phone_number = ''.join(phone_number)
    
    return phone_number