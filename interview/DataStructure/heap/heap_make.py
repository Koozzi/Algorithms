def heapify_down(K, N):
    while 2*K+2 < N:    
        L, R = 2*K+1, 2*K+2
        tmp = [(K, A[K]), (L, A[L]), (R, A[R])]
        tmp = sorted(tmp, key=lambda x: -x[1])
        M = tmp[0][0]

        if K != M:
            A[K], A[M] = A[M], A[K]
            K = M
        else:
            break            

def heap_make(A):
    N = len(A)
    for K in range(N-1, -1, -1):
        heapify_down(K, N)

if __name__=="__main__":
    A = [2, 8, 6, 1, 10, 15, 3, 12, 11]
    heap_make(A)
    print(*A)
    