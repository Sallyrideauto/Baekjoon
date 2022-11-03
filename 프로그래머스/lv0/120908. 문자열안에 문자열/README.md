# [level 0] 문자열안에 문자열 - 120908 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120908) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">문자열 <code style="user-select: auto;">str1</code>, <code style="user-select: auto;">str2</code>가 매개변수로 주어집니다. <code style="user-select: auto;">str1</code> 안에 <code style="user-select: auto;">str2</code>가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">str1</code>의 길이 ≤ 100</li>
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">str2</code>의 길이 ≤ 100</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">str1</th>
<th style="user-select: auto;">str2</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">"ab6CDE443fgh22iJKlmn1o"</td>
<td style="user-select: auto;">"6CD"</td>
<td style="user-select: auto;">1</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">"ppprrrogrammers"</td>
<td style="user-select: auto;">"pppp"</td>
<td style="user-select: auto;">2</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">"ab<code style="user-select: auto;">6CD</code>E443fgh22iJKlmn1o" <code style="user-select: auto;">str1</code>에 <code style="user-select: auto;">str2</code>가 존재하므로 1을 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">"ppprrrogrammers" <code style="user-select: auto;">str1</code>에 <code style="user-select: auto;">str2</code>가 없으므로 2를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges