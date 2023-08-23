function solution(s) {
    let regex = /^\d{6}$|^\d{4}$/;
    return regex.test(s);
}

// https://www.techiedelight.com/ko/check-if-variable-is-string-javascript/
// https://cherish-my-codes.tistory.com/entry/Programmers-Level1-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%8B%A4%EB%A3%A8%EA%B8%B0-%EA%B8%B0%EB%B3%B8JavaScript