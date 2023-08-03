function solution(slice, n) {
    var answer = 0;
    
    a = Math.floor(n / slice)
    b = n % slice
    
    if (b === 0) {
        answer = a * 1;
    } else {
        answer = a * 1 + 1;
    }
    
    return answer;
}