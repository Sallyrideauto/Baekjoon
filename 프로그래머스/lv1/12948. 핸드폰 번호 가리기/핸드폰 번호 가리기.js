function solution(phone_number) {
    var length = phone_number.length;
    var lastFourDigits = phone_number.substring(length - 4);
    var hiddenDigits = "*".repeat(length - 4);
    
    return hiddenDigits + lastFourDigits;
}

// 위 코드는 solution 함수를 정의하여 전화번호의 뒷 4자리를 제외한 나머지 숫자를 *로 가리는 기능을 수행합니다. 
// substring 메서드를 사용하여 뒷 4자리를 가져온 후, 나머지 자릿수에 대해 *을 반복하여 숨깁니다. 
// 마지막으로 숨긴 문자열과 뒷 4자리를 이어서 반환합니다.