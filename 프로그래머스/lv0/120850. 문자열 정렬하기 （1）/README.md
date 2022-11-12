# [level 0] 문자열 정렬하기 (1) - 120850 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120850) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.10 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">문자열 <code style="user-select: auto;">my_string</code>이 매개변수로 주어질 때, <code style="user-select: auto;">my_string</code> 안에 있는 숫자만 골라 오름차순 정렬한 리스트를&nbsp;return 하도록 solution 함수를 작성해보세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">my_string</code>의 길이 ≤ 100</li>
<li style="user-select: auto;"><code style="user-select: auto;">my_string</code>에는 숫자가 한 개 이상 포함되어 있습니다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">my_string</code>은 영어 소문자 또는 0부터 9까지의 숫자로 이루어져 있습니다.
- - -</li>
</ul>

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">my_string</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">"hi12392"</td>
<td style="user-select: auto;">[1, 2, 2, 3, 9]</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">"p2o4i8gj2"</td>
<td style="user-select: auto;">[2, 2, 4, 8]</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">"abcde0"</td>
<td style="user-select: auto;">[0]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">"hi12392"에 있는 숫자 1, 2, 3, 9, 2를 오름차순 정렬한 [1, 2, 2, 3, 9]를 return 합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">"p2o4i8gj2"에 있는 숫자 2, 4, 8, 2를 오름차순 정렬한 [2, 2, 4, 8]을 return 합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #3</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">"abcde0"에 있는 숫자 0을 오름차순 정렬한 [0]을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges