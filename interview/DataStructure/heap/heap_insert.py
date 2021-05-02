def heap_insert(A, new_num):
    A.append(new_num)
    K = len(A)-1
    while K > 0 and A[(K-1)//2] < A[K]:
        A[K], A[(K-1)//2] = A[(K-1)//2], A[K]
        K = (K-1)//2

if __name__=="__main__":
    A = [15, 12, 6, 11, 10, 2, 3, 1, 8]
    heap_insert(A, 14)
    print(*A)