function solution(n) {
    var answer = 0;
    
    a = Math.floor(n / 7)
    b = n % 7
    
    if (b === 0) {
        answer = a * 1
    } else {
        answer = a * 1 + 1
    }
    
    return answer;
}