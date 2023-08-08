function solution(n) {
    let answer = '';
    for (let i = 0; i < n; i++) {
        if (i % 2 === 0) {
            answer += '수';
        } else {
            answer += '박';
        }
    }
    return answer;
}

// 위 코드에서 solution 함수는 n을 입력으로 받아서 길이가 n인 패턴을 유지하는 문자열을 생성하고 반환합니다.
// 반복문을 이용하여 인덱스 i가 짝수인 경우에는 "수"를, 홀수인 경우에는 "박"을 answer 문자열에 추가하여 패턴을 생성합니다.

