function solution(n)
{
    var answer = 0;
    var m = String(n);
    
    for (let i = 0; i < m.length; i++) {
        answer += parseInt(m[i]);
    }
    
    return answer;
}

// 참고 https://velog.io/@hye_rin/JavaScript-Programmers-Lv.1-%EC%9E%90%EB%A6%BF%EC%88%98-%EB%8D%94%ED%95%98%EA%B8%B0