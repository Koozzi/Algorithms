def solution(genres, plays):
    answer = []

    genre_total_play = {}
    genre_music_info = {}

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_total_play:
            genre_total_play[genre] = play
            genre_music_info[genre] = [(idx, play)]
        else:
            genre_total_play[genre] += play
            genre_music_info[genre].append((idx, play))

    # genre_total_play = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)
    genre_total_play = sorted(genre_total_play.items(), key=lambda x: -x[1])

    for genre in genre_total_play:
        genre_music = genre_music_info[genre[0]]
        genre_music = sorted(genre_music, key=lambda x: (-x[1], x[0]))

        for idx, item in enumerate(genre_music):
            if idx == 2: break
            answer.append(item[0])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# [4, 1, 3, 0]