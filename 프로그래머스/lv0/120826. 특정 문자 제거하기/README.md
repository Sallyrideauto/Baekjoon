# [level 0] 특정 문자 제거하기 - 120826 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120826) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">문자열 <code style="user-select: auto;">my_string</code>과 문자 <code style="user-select: auto;">letter</code>이 매개변수로 주어집니다. <code style="user-select: auto;">my_string</code>에서 <code style="user-select: auto;">letter</code>를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">my_string</code>의 길이 ≤ 100</li>
<li style="user-select: auto;"><code style="user-select: auto;">letter</code>은 길이가 1인 영문자입니다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">my_string</code>과 <code style="user-select: auto;">letter</code>은 알파벳 대소문자로 이루어져 있습니다.</li>
<li style="user-select: auto;">대문자와 소문자를 구분합니다.</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">my_string</th>
<th style="user-select: auto;">letter</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">"abcdef"</td>
<td style="user-select: auto;">"f"</td>
<td style="user-select: auto;">"abcde"</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">"BCBdbe"</td>
<td style="user-select: auto;">"B"</td>
<td style="user-select: auto;">"Cdbe"</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">"abcdef" 에서 "f"를 제거한 "abcde"를 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">"BCBdbe" 에서 "B"를 모두 제거한 "Cdbe"를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges