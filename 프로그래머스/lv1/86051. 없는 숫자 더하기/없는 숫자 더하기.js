function solution(numbers) {
    var answer = 0;
    
    for (let i = 0; i < 10; i++) {
        if(!numbers.includes(i)) answer += i;
        // numbers가 i를 포함하지 않는다면, answer에 그 i 값들을 더할 것
    }
    
    return answer;
}

// 출처 https://velog.io/@ne_ol/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%86%EB%8A%94-%EC%88%AB%EC%9E%90-%EB%8D%94%ED%95%98%EA%B8%B0JavaScript