"""
다솜이가 필요한 플라스틱 숫자의 세트 수는 각 숫자가 몇 개 필요한지를 세면 된다. 
이때, 6과 9는 서로 뒤집어서 사용할 수 있으므로, 6과 9의 개수를 더한 후, 2로 나누어 올림한 값이 필요한 세트의 개수가 된다.

즉, 우선 각 숫자가 몇 개 필요한지 세고, 6과 9는 더한 후 2로 나누어 올림한 값을 구하면 된다. 
이를 파이썬 코드로 구현하면 다음과 같다.
"""

import math

n = input()  # 다솜이의 방 번호
count = [0] * 10  # 각 숫자가 몇 개 필요한지를 저장할 리스트

for digit in n:
    count[int(digit)] += 1

# 6과 9는 뒤집어서 사용할 수 있으므로, 두 수의 개수를 합산하고 2로 나누어 올림한다.
count[6] = math.ceil((count[6] + count[9]) / 2)
count[9] = 0  # 이미 6의 개수를 합산했으므로, 9는 더 이상 필요하지 않다.

print(max(count))  # 필요한 세트의 최솟값은 가장 많이 필요한 숫자의 개수와 같다.

"""
위 코드에서, count 리스트의 인덱스 i는 숫자 i가 몇 개 필요한지를 저장한다. 
이후, 6과 9를 합산하고, 9는 더 이상 필요하지 않으므로 0으로 설정한다. 
마지막으로, 필요한 세트의 최솟값은 가장 많이 필요한 숫자의 개수와 같으므로, max(count)를 출력한다.
"""