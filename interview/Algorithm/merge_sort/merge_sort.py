def merge_two_sorted_list(A, first, last):
    mid = (first + last) // 2
    i, j = first, mid + 1
    B = []

    while i <= mid and j <= last:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        elif A[i] > A[j]:
            B.append(A[j])
            j += 1
    
    # 아래 2개의 for문 중 하나만 돌아갈 것임.
    for k in range(i, mid + 1):
        B.append(A[k])
    
    for k in range(j, last + 1):
        B.append(A[k])
    
    for i in range(first, last + 1):
        A[i] = B[i - first]


def merge_sort(A, first, last):
    if first >= last:
        return A
    
    merge_sort(A, first, (first + last) // 2)
    merge_sort(A, (first + last) // 2 + 1, last)
    merge_two_sorted_list(A, first, last)

if __name__=="__main__":
    A = [4,3,5,1,7,4,4,6,2,4]
    merge_sort(A, 0, len(A)-1)
    print(*A)
    