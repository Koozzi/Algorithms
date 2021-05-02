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

def heap_sort(A):
    if not A:
        return None    
    
    for k in range(len(A)-1, 0, -1):
        A[0], A[k] = A[k], A[0]
        heapify_down(0, k+1)

if __name__=="__main__":
    A = [15, 12, 6, 11, 10, 2, 3, 1, 8]
    heap_sort(A)
    print(*A)