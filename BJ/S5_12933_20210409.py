from sys import stdin

prev_dictionary = {
    'q': 'k',
    'u': 'q',
    'a': 'u',
    'c': 'a',
    'k': 'c',
}

duck_sound = list(stdin.readline().strip())
visit = [False for _ in range(len(duck_sound))]
answer = 0

for idx,sound in enumerate(duck_sound):

    if sound == 'q' and not visit[idx]:
        sound_count = 1
        visit[idx] = True
        prev_sound = 'q'

        for sub_idx, sub_sound in enumerate(duck_sound[idx+1:],start=idx+1): 
            if not visit[sub_idx] and prev_sound == prev_dictionary[sub_sound]:
                sound_count += 1
                visit[sub_idx] = True
                prev_sound = sub_sound

        if sound_count % 5 == 0:
            answer += 1
        else:
            print(-1)
            exit()
    
    elif sound != 'q' and not visit[idx]:
        print(-1)
        exit()

print(answer)