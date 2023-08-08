function solution(s) {
    const middleIndex = Math.floor(s.length / 2);
    return s.length % 2 === 0 ? s.substr(middleIndex - 1, 2) : s.charAt(middleIndex);
}

// 위 코드는 solution 함수를 정의하여 주어진 문자열 s의 가운데 글자 또는 가운데 두 글자를 반환하는 기능을 수행합니다.
// Math.floor를 사용하여 가운데 인덱스를 계산하고, substr 또는 charAt 메서드를 사용하여 가운데 글자 또는 가운데 두 글자를 추출하여 반환합니다.

