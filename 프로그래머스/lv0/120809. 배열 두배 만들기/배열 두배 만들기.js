function solution(numbers) {
    var answer = [];
    
    numbers.forEach(function (elm) {
        answer.push(elm * 2);
    });
    
    return answer;
}