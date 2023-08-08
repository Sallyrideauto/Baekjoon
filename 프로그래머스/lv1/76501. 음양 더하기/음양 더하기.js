function solution(absolutes, signs) {
    let sum = 0;
    for (let i = 0; i < absolutes.length; i++) {
        if (signs[i]) {
            sum += absolutes[i];
        } else {
            sum -= absolutes[i];
        }
    }
    return sum;
}

// 위 코드에서 solution 함수는 absolutes 배열과 signs 배열을 입력으로 받아서 해당 정수들의 합을 계산하고 반환합니다.
// 반복문을 이용하여 absolutes 배열의 각 요소에 대해 signs 배열의 값을 확인하여 양수인 경우에는 더하고 음수인 경우에는 빼주어 합을 계산합니다.

