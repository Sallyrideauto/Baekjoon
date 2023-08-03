function solution(numbers) {
    // reduce() : 배열의 각 요소에 대해 주어진 리듀서 함수를 실행하고, 하나의 결과값을 반환
    return numbers.reduce((sum, current) => sum + current) / numbers.length;
}