# [level 0] 각도기 - 120829 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120829) 

### 성능 요약

메모리: 9.99 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 각 <code style="user-select: auto;">angle</code>이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">예각 : 0 &lt; <code style="user-select: auto;">angle</code> &lt; 90</li>
<li style="user-select: auto;">직각 : <code style="user-select: auto;">angle</code> = 90</li>
<li style="user-select: auto;">둔각 : 90 &lt; <code style="user-select: auto;">angle</code> &lt; 180</li>
<li style="user-select: auto;">평각 : <code style="user-select: auto;">angle</code> = 180</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">0 &lt; <code style="user-select: auto;">angle</code> ≤ 180</li>
<li style="user-select: auto;"><code style="user-select: auto;">angle</code>은 정수입니다.</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">angle</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">70</td>
<td style="user-select: auto;">1</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">91</td>
<td style="user-select: auto;">3</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">180</td>
<td style="user-select: auto;">4</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">angle</code>이 70이므로 예각입니다. 따라서 1을 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">angle</code>이 91이므로 둔각입니다. 따라서 3을 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">angle</code>이 180이므로 평각입니다. 따라서 4를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges