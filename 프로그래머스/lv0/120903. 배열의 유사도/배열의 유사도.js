function solution(s1, s2) {
    return s1.filter((el) => s2.indexOf(el) >= 0).length;
}