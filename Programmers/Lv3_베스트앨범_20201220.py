def solution(genres, plays):
    answer = []
            
    genre_total_play = {}
    genre_dic = {}

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_dic:
            genre_dic[genre] = [(play, idx)]
            genre_total_play[genre] = play
        else:
            genre_dic[genre].append((play, idx))
            genre_total_play[genre] += play

    sorted_total_play = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)

    for key in sorted_total_play:
        play_list = genre_dic[key[0]]
        play_list = sorted(play_list, key=lambda x: (-x[0], x[1]))

        for i in range(len(play_list)):
            if i == 2:
                break
            answer.append(play_list[i][1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))