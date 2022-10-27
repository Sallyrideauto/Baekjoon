# [level 0] 숫자 비교하기 - 120807 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120807) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">정수 <code style="user-select: auto;">num1</code>과 <code style="user-select: auto;">num2</code>가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">0 ≤ <code style="user-select: auto;">num1</code> ≤ 10,000</li>
<li style="user-select: auto;">0 ≤ <code style="user-select: auto;">num2</code> ≤ 10,000</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">num1</th>
<th style="user-select: auto;">num2</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">-1</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">11</td>
<td style="user-select: auto;">11</td>
<td style="user-select: auto;">1</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">7</td>
<td style="user-select: auto;">99</td>
<td style="user-select: auto;">-1</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 설명 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">num1</code>이 2이고 <code style="user-select: auto;">num2</code>가 3이므로 다릅니다. 따라서 -1을 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 설명 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">num1</code>이 11이고 <code style="user-select: auto;">num2</code>가 11이므로 같습니다. 따라서 1을 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 설명 #3</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">num1</code>이 7이고 <code style="user-select: auto;">num2</code>가 99이므로 다릅니다. 따라서 -1을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges