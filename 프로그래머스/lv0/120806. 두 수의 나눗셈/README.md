# [level 0] 두 수의 나눗셈 - 120806 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120806) 

### 성능 요약

메모리: 10 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">정수 <code style="user-select: auto;">num1</code>과 <code style="user-select: auto;">num2</code>가 매개변수로 주어질 때, <code style="user-select: auto;">num1</code>을 <code style="user-select: auto;">num2</code>로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.</p>

<hr style="user-select: auto;">

<h4 style="user-select: auto;">제한사항</h4>

<ul style="user-select: auto;">
<li style="user-select: auto;">0 &lt; <code style="user-select: auto;">num1</code> ≤ 100</li>
<li style="user-select: auto;">0 &lt; <code style="user-select: auto;">num2</code> ≤ 100</li>
</ul>

<hr style="user-select: auto;">

<h4 style="user-select: auto;">입출력 예</h4>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">num1</th>
<th style="user-select: auto;">num2</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">1500</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">7</td>
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">2333</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">16</td>
<td style="user-select: auto;">62</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h4 style="user-select: auto;">입출력 예 설명</h4>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">num1</code>이 3, <code style="user-select: auto;">num2</code>가 2이므로 3 / 2 = 1.5에 1,000을 곱하면 1500이 됩니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">num1</code>이 7, <code style="user-select: auto;">num2</code>가 3이므로 7 / 3 = 2.33333...에 1,000을 곱하면 2333.3333.... 이 되며, 정수 부분은 2333입니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #3</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">num1</code>이 1, <code style="user-select: auto;">num2</code>가 16이므로 1 / 16 = 0.0625에 1,000을 곱하면 62.5가 되며, 정수 부분은 62입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges