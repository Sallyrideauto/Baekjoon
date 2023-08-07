function solution(array, n) {
    var numbers = array.filter(item => item === n)
    var answer = numbers.length;
    return answer;
}