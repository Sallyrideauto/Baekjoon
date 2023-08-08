function solution(s) {
    var arr = s.split(' ');
    
    arr.sort((a, b) => b - a);
    
    var max = arr[0]
    var min = arr[arr.length - 1]
    
    return min + " " + max;
}

// https://zzemal.tistory.com/70