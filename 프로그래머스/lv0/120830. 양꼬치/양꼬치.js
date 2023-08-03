function solution(n, k) {
    var answer = n * 12000 + k * 2000 - Math.floor(n / 10) * 2000;
    return answer;
}