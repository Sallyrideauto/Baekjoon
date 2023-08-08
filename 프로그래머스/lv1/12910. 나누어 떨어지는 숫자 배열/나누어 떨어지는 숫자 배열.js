function solution(arr, divisor) {
    var answer = [];
    
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] % divisor === 0) {
            answer.push(arr[i]);
        }
    }
    answer.sort((a, b) => a - b);
    
    if (answer.length === 0) {
        answer.push(-1);
    }
    
    return answer;
}

// https://celltong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-JavaScript-level-1-%EB%82%98%EB%88%84%EC%96%B4-%EB%96%A8%EC%96%B4%EC%A7%80%EB%8A%94-%EC%88%AB%EC%9E%90-%EB%B0%B0%EC%97%B4