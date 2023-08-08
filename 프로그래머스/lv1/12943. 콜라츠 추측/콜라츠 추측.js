function solution(num) {
    let count = 0;
    while (num !== 1) {
        if (num % 2 === 0) {
            num /= 2;
        } else {
            num = num * 3 + 1;
        }
        count++;
        if (count === 500) {
            return -1;
        }
    }
    return count;
}

// 위 코드에서 solution 함수는 주어진 수 num에 대해 Collatz 추측을 반복하여 1이 되기까지 걸리는 횟수를 계산하고 반환합니다.
// 1이 될 때까지 반복하는 동안 짝수인 경우 2로 나누고, 홀수인 경우 3을 곱하고 1을 더해주는 작업을 반복합니다.
// 그리고 작업 횟수가 500회를 초과하면 -1을 반환합니다.

