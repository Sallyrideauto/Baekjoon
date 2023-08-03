function solution(arr) {
    return arr.reduce((sum, current) => sum + current) / arr.length;
}