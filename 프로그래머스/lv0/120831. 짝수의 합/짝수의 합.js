function solution(n) {
    var answer = 0;
    
    for(var i = 1; i <= n; i++){
        if(i % 2 === 0){
            var answer = answer + i;
        }
    }
    
    return answer
}