"""
해당 문제는 Disjoint Set (서로소 집합) 자료구조를 이용하여 해결할 수 있습니다.
Disjoint Set은 여러 개의 원소가 있을 때, 이들이 서로소 관계인지를 판별하는 자료구조입니다.

Disjoint Set은 두 가지 주요 연산이 있습니다.

make-set(x): 새로운 원소 x를 포함하는 새로운 집합을 만듭니다.
union(x,y): x가 속한 집합과 y가 속한 집합을 합칩니다.
이 문제에서는 이 두 가지 연산이 합집합 연산과 같은 기능을 수행합니다.

Disjoint Set을 구현할 때, 부모 노드를 저장하는 parent 배열과 각 집합의 크기를 저장하는 size 배열을 이용합니다. parent 배열의 초기값은 자기 자신을 가리키고, size 배열의 초기값은 1로 설정합니다.

그리고 두 원소가 같은 집합에 속해 있는지를 확인할 때는 find(x) 함수를 이용합니다. 이 함수는 x가 속한 집합의 대표 원소, 즉 루트 노드를 반환합니다. 루트 노드는 자기 자신을 가리키므로, 루트 노드가 같은지를 비교하여 두 원소가 같은 집합에 속해 있는지를 판별할 수 있습니다.

이제 위에서 설명한 Disjoint Set을 이용하여 문제를 해결 해 보겠습니다.
"""

import sys

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n+1)]
size = [1 for i in range(n+1)]

for i in range(m):
    op, a, b = map(int, sys.stdin.readline().split())
    if op == 0:
        pa, pb = find(a), find(b)
        if pa != pb:
            if size[pa] > size[pb]:
                pa, pb = pb, pa
            parent[pa] = pb
            size[pb] += size[pa]
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

            
"""
위 코드에서는 find 함수를 경로 압축(path compression) 기법을 이용하여 최적화하였습니다. 
경로 압축은 find 함수를 호출할 때마다, 해당 노드에서 루트 노드까지의 경로 상에 있는 모든 노드의 parent를 루트 노드로 갱신하는 기법입니다. 
이렇게 하면, 다음에 같은 노드를 찾을 때에는 루트 노드를 한 번에 찾을 수 있으므로, 시간 복잡도를 개선할 수 있습니다.
"""