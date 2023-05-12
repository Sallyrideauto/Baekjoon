from collections import defaultdict

def solution(genres, plays):
    # 장르별 재생 횟수와 노래 정보를 저장할 딕셔너리 생성
    genre_play_count = defaultdict(int)
    song_info = defaultdict(list)

    # 장르별 재생 횟수와 노래 정보 카운트
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        genre_play_count[genre] += play
        song_info[genre].append((i, play))

    # 장르별 재생 횟수를 기준으로 내림차순 정렬
    sorted_genre_play_count = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)

    answer = []
    # 장르별로 최대 두 개의 노래 선택하여 앨범에 추가
    for genre, _ in sorted_genre_play_count:
        song_info[genre].sort(key=lambda x: (-x[1], x[0]))  # 재생 횟수와 고유 번호를 기준으로 정렬
        answer.extend([idx for idx, _ in song_info[genre][:2]])  # 최대 두 개의 노래 추가

    return answer

"""
위 코드에서는 defaultdict를 사용하여 장르별 재생 횟수와 노래 정보를 저장합니다. 
먼저 genre_play_count 딕셔너리에는 각 장르별로 총 재생 횟수를 카운트합니다. 
그리고 song_info 딕셔너리에는 각 장르별로 (고유 번호, 재생 횟수) 형태의 노래 정보를 저장합니다.

다음으로 genre_play_count를 재생 횟수를 기준으로 내림차순으로 정렬합니다. 
그리고 정렬된 순서대로 장르별로 노래 정보를 가져와서 재생 횟수와 고유 번호를 기준으로 정렬합니다. 
이후 최대 두 개의 노래를 선택하여 answer 리스트에 추가합니다.

최종적으로 answer 리스트를 반환하면 베스트 앨범에 수록된 노래의 고유 번호를 순서대로 얻을 수 있습니다.
"""