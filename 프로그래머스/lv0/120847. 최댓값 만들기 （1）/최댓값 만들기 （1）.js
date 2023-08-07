function solution(numbers) {
    numbers.sort((a, b) => b - a);
    var answer = numbers[0] * numbers[1];
    return answer;
}

// 모던 자바스크립트 Deep Dive 531p