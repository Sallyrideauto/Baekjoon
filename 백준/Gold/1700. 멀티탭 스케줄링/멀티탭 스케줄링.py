def min_unplugging_count(N, K, appliances):
    multitap = []
    unplugging_count = 0

    for i in range(K):
        if appliances[i] in multitap:
            continue

        if len(multitap) < N:
            multitap.append(appliances[i])
        else:
            max_idx = -1
            max_usage = -1

            for j in range(N):
                try:
                    usage = appliances[i + 1:].index(multitap[j])
                except ValueError:
                    usage = 101

                if max_usage < usage:
                    max_usage = usage
                    max_idx = j

            multitap[max_idx] = appliances[i]
            unplugging_count += 1

    return unplugging_count

def main():
    N, K = map(int, input().split())
    appliances = list(map(int, input().split()))
    print(min_unplugging_count(N, K, appliances))

if __name__ == "__main__":
    main()

"""
이 프로그램은 min_unplugging_count 함수를 사용하여 주어진 멀티탭 구멍의 개수 N과 
전기 용품의 총 사용횟수 K에 대해 플러그를 빼는 최소 횟수를 구합니다. 
결과를 출력합니다.
"""