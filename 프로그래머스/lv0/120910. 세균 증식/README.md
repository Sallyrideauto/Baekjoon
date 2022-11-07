# [level 0] 세균 증식 - 120910 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120910) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 <code style="user-select: auto;">n</code>과 경과한 시간 <code style="user-select: auto;">t</code>가 매개변수로 주어질 때 <code style="user-select: auto;">t</code>시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">n</code> ≤ 10</li>
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">t</code> ≤ 15</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">n</th>
<th style="user-select: auto;">t</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">10</td>
<td style="user-select: auto;">2048</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">7</td>
<td style="user-select: auto;">15</td>
<td style="user-select: auto;">229,376</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">처음엔 2마리, 1시간 후엔 4마리, 2시간 후엔 8마리, ..., 10시간 후엔 2048마리가 됩니다. 따라서 2048을 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">처음엔 7마리, 1시간 후엔 14마리, 2시간 후엔 28마리, ..., 15시간 후엔 229376마리가 됩니다. 따라서 229,376을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges