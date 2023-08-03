// https://shinjekim.github.io/algorithms/2018/09/17/javascript-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level1-%ED%95%98%EC%83%A4%EB%93%9C-%EC%88%98/

function solution(x) {
    var sum = 0;
    var arr = String(x).split('');
    
    for (var i = 0; i < arr.length; i++) {
        sum += Number(arr[i]);
    }
    
    return (x % sum === 0) ? true : false;
}