# [level 0] 머쓱이보다 키 큰 사람 - 120585 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120585) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 머쓱이네 반 친구들의 키가 담긴 정수 배열 <code style="user-select: auto;">array</code>와 머쓱이의 키 <code style="user-select: auto;">height</code>가 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">array</code>의 길이 ≤ 100</li>
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">height</code> ≤ 200</li>
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">array</code>의 원소 ≤ 200</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">array</th>
<th style="user-select: auto;">height</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">[149, 180, 192, 170]</td>
<td style="user-select: auto;">167</td>
<td style="user-select: auto;">3</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">[180, 120, 140]</td>
<td style="user-select: auto;">190</td>
<td style="user-select: auto;">0</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">149, 180, 192, 170 중 머쓱이보다 키가 큰 사람은 180, 192, 170으로 세 명입니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">180, 120, 140 중 190보다 큰 수는 없으므로 0명입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges