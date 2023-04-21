def main():
    # 입력 받기
    n = int(input())
    coords = list(map(int, input().split()))

    # 좌표 압축 적용
    unique_coords = sorted(set(coords))
    coord_mapping = {coord: index for index, coord in enumerate(unique_coords)}

    # 결과 출력
    compressed_coords = [coord_mapping[coord] for coord in coords]
    print(" ".join(map(str, compressed_coords)))

if __name__ == "__main__":
    main()

"""
이 프로그램은 주어진 좌표에 대해 좌표 압축을 적용하고, 결과를 출력합니다. 
입력으로 주어진 좌표의 개수 N과 좌표들을 받아서 좌표 압축을 수행한 후, 
결과를 공백 한 칸으로 구분하여 출력합니다.
"""