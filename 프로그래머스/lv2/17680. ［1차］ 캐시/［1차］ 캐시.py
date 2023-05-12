# LRU (Least Recently Used) 알고리즘을 이용하여 DB 캐시의 크기에 따른 실행 시간을 측정하는 프로그램

from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cache = deque(maxlen=cacheSize)
    time = 0

    for city in cities:
        city_lower = city.lower()
        if city_lower in cache:
            cache.remove(city_lower)
            cache.append(city_lower)
            time += 1
        else:
            cache.append(city_lower)
            time += 5

    return time

"""
위의 코드는 입력으로 주어진 cacheSize와 cities에 따라 LRU 알고리즘을 적용하여 실행 시간을 계산합니다. 
먼저, 캐시 크기가 0일 경우 모든 도시에 대해 cache miss가 발생하므로 실행 시간은 len(cities) * 5가 됩니다.

그렇지 않은 경우, deque를 사용하여 캐시를 구현하고, cacheSize를 초과하는 경우 가장 오래전에 사용된 도시를 제거합니다. 
도시가 캐시에 있는 경우에는 해당 도시를 제거하고 다시 캐시의 가장 최근에 사용된 위치로 추가합니다. 
실행 시간은 cache hit일 때는 1, cache miss일 때는 5를 더하면서 계산됩니다.
"""