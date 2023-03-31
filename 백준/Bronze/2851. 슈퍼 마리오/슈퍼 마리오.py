mushrooms = []
for i in range(10):
    mushrooms.append(int(input()))

total_score = 0
for i in range(10):
    total_score += mushrooms[i]
    if total_score >= 100:
        break
        
if abs(total_score - 100) <= abs(total_score - mushrooms[i] - 100):
    print(total_score)
else:
    print(total_score - mushrooms[i])

"""
위 코드는 각 버섯의 점수를 리스트에 저장한 후, 
리스트를 순회하면서 버섯의 점수를 더해가며 100에 가까운 수를 만들어내는 방법으로 문제를 해결합니다.
마지막으로, 100과 가장 가까운 값을 선택하여 출력합니다.
"""