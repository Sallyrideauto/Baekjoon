function solution(num_list) {
    var answer = [0, 0];
    
    for (let a of num_list) {
        answer[a % 2] += 1
    }
    
    return answer;
    
}

// https://velog.io/@gagaeun/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A7%9D%EC%88%98-%ED%99%80%EC%88%98-%EA%B0%9C%EC%88%98