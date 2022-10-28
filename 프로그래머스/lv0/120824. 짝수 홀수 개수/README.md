# [level 0] 짝수 홀수 개수 - 120824 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120824) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">정수가 담긴 리스트&nbsp;<code style="user-select: auto;">num_list</code>가 주어질 때, <code style="user-select: auto;">num_list</code>의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">num_list</code>의 길이 ≤ 100</li>
<li style="user-select: auto;">0 ≤ <code style="user-select: auto;">num_list</code>의 원소 ≤ 1,000</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">num_list</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">[1, 2, 3, 4, 5]</td>
<td style="user-select: auto;">[2, 3]</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">[1, 3, 5, 7]</td>
<td style="user-select: auto;">[0, 4]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">[1, 2, 3, 4, 5]에는 짝수가 2, 4로 두 개, 홀수가 1, 3, 5로 세 개 있습니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">[1, 3, 5, 7]에는 짝수가 없고 홀수가 네 개 있습니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges