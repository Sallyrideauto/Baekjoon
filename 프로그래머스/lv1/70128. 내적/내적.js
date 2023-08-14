function solution(a, b) {
    return (a.map((cur, i) => cur * b[i])).reduce((a, b) => a + b);
}

// https://velog.io/@ne_ol/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%82%B4%EC%A0%81JavaScript