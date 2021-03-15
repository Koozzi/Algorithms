def solution(key, lock):
    answer = True

    key_N, key_M = len(key), len(key[0])
    lock_N, lock_M = len(lock), len(lock[0])

    # 자물쇠의 모든 부분이 돌기 영역이면?

    left, right, top, bottom = lock_N-1, 0, lock_M-1, 0
    for i in range(lock_N):
        for j in range(lock_M):
            if lock[i][j] == 0:
                left = min(left, j)
                top = min(top, i)
                right = max(right, j)
                bottom = max(bottom, i)

    print(top, left, bottom, right)
    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	))