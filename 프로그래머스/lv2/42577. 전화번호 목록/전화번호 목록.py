def solution(phone_book):
    phone_book.sort()  # 전화번호를 정렬하여 비교하기 쉽게 함

    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False

    return True

"""
위 코드에서는 전화번호부를 받아와서 sort 함수를 사용하여 전화번호를 정렬합니다. 
그런 다음 반복문을 통해 인접한 두 전화번호를 비교하여 접두어 관계인지 확인합니다. 
한 번호가 다른 번호의 접두어인 경우 False를 반환하고, 
모든 번호를 비교한 후에도 접두어 관계가 없으면 True를 반환합니다.
"""